import helper
import threading

person1 = helper.Person(0, 0, 0, 0, 0, '1')
person2 = helper.Person(0, 0, 0, 0, 0, '2')

fair = helper.BordemFair([person1, person2])

growing_1 = threading.Thread(target=helper.growing, args=(person1,))
growing_1.start()
growing_2 = threading.Thread(target=helper.growing, args=(person2,))
growing_2.start()
fighting = threading.Thread(target=helper.fighting, args=(fair,))
fighting.start()
