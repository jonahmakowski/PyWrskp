import krpc
from time import sleep

# User inputs
orbit_height = 120000
open_solar = True
open_antennas = True
open_radiators = True


# krpc Constants
conn = krpc.connect(name='To Orbit!')
vessel = conn.space_center.active_vessel

# Data streaming
ut = conn.add_stream(getattr, conn.space_center, 'ut')
altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
apoapsis = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')
periapsis = conn.add_stream(getattr, vessel.orbit, 'periapsis_altitude')
thrust = conn.add_stream(getattr, vessel, 'thrust')
mass = conn.add_stream(getattr, vessel, 'mass')
parts_stream = conn.add_stream(getattr, vessel.parts, 'all')
engine_stream = conn.add_stream(getattr, vessel.parts, 'engines')
stage_stream = conn.add_stream(getattr, vessel.control, 'current_stage')

# Setup
vessel.auto_pilot.engage()
vessel.control.sas = False
vessel.control.rcs = False
vessel.control.reaction_wheels = True
vessel.lights = True


def get_twr():
    return thrust() / mass() * vessel.orbit.body.surface_gravity


def stage_check():
    current_stage = stage_stream()

    # Loop through stages from current to previous
    for stage in range(current_stage, -1, -1):
        # Get parts in the current stage
        stage_parts = [p for p in parts_stream() if p.stage == stage]

        print(stage_parts)

        # Check if any parts have fuel in this stage
        dry_mass = 0
        mass = 0
        for part in stage_parts:
            dry_mass += part.dry_mass
            mass += part.mass

        has_fuel = mass - dry_mass != 0

        print(mass)
        print(dry_mass)

        # If no parts have fuel, activate engines in the stage below
        if not has_fuel and stage > 0:
            vessel.control.activate_next_stage()


def map_value(range1: float, range2: float, value: float):
    ratio = range2 / range1
    return value * ratio


def proportional_reaction(where_am, where_want, adjust=1):
    return (where_am - where_want) * adjust


# Taking off
vessel.control.activate_next_stage()
vessel.control.throttle = 1
vessel.auto_pilot.target_pitch_and_heading(90, 90)
while vessel.flight(vessel.orbit.body.reference_frame).vertical_speed < 100:
    stage_check()

# Gravity Turn
while altitude() < 70100:
    if apoapsis() < orbit_height:
        vessel.control.throttle = 1
        while apoapsis() < 80000:
            turn = map_value(90, 70000, altitude())
            vessel.auto_pilot.target_pitch_and_heading(90-turn, 90)
            twr = get_twr()

            if twr > 2:
                reaction = proportional_reaction(twr, 1.5)
                vessel.control.throttle -= reaction
            elif twr < 1.2:
                reaction = proportional_reaction(twr, 1.5)
                if not vessel.control.throttle + reaction > 1:
                    vessel.control.throttle += reaction
                else:
                    vessel.control.throttle = 1
            stage_check()
        vessel.control.throttle = 0

# Coasting to apoapsis
vessel.auto_pilot.disengage()
vessel.control.sas = True
vessel.control.sas_mode = vessel.control.sas_mode.prograde
with conn.stream(vessel.orbit, 'time_to_apoapsis') as time_until_apoapsis:
    start_time = ut()
    start_time_until = time_until_apoapsis()
    conn.warp_to(start_time+start_time_until-50)
    while time_until_apoapsis > 10:
        pass

# Opening gear
if open_solar:
    for part in vessel.parts.solar_panels:
        if part.deployable:
            part.deployed = True

if open_radiators:
    for part in vessel.parts.radiators:
        if part.deployable:
            part.deployed = True

if open_antennas:
    for part in vessel.parts.antennas:
        if part.deployable:
            part.deployed = True

# Raise periapsis
vessel.control.throttle = 1
while not apoapsis() < orbit_height:
    stage_check()
vessel.control.throttle = 0

# Warp to apoapsis
with conn.stream(vessel.orbit, 'time_to_apoapsis') as time_until_apoapsis:
    start_time = ut()
    start_time_until = time_until_apoapsis()
    conn.warp_to(start_time+start_time_until-50)
    while time_until_apoapsis > 10:
        pass

# Raise periapsis
vessel.control.throttle = 1
while not orbit_height - 1000 < periapsis() < orbit_height + 1000:
    stage_check()
vessel.control.throttle = 0

# All Done!
print('All done')
for _ in range(10):
    vessel.lights = False
    sleep(0.01)
    vessel.lights = True
    sleep(0.01)
