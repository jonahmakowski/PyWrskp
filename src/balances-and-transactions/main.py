from datetime import datetime, date, timedelta


class BalancesAndTransactions:
    def __init__(self, transaction_history, balances):
        """
        Expected format:
        [{'amount':100, 'date':datetime}, {'amount':100, 'date':datetime}]
        """
        self.transaction_history = transaction_history
        self.balances_original = balances
        self.balances_with_check = []

    def check_balances(self):
        balances = self.balances_original.copy()
        del balances[0]
        prev_balance = self.balances_original[0]
        for balance in balances:
            transactions = self.transactions_between_dates(prev_balance['date'].split()[0],
                                                           balance['date'].split()[0],
                                                           amount_only=True)
            should_be = sum(transactions) + prev_balance['amount']
            checked = balance.copy()
            checked['status'] = 'Green' if should_be == balance['amount'] else 'Red'
            self.balances_with_check.append(checked)
            if should_be == balance['amount']:
                prev_balance = balance

    def transactions_from_date(self, date, amount_only=False):
        transactions = []
        for transaction in self.transaction_history:
            if transaction['date'].split()[0] == date:
                if amount_only:
                    transactions.append(transaction['amount'])
                else:
                    transactions.append(transaction)

        return transactions

    def transactions_between_dates(self, start_date, end_date, amount_only=False):
        dates = self.get_dates_between(start_date, end_date)
        transactions = []
        for date in dates:
            transactions.extend(self.transactions_from_date(date, amount_only=amount_only))
        return transactions

    @staticmethod
    def get_dates_between(start_date, end_date):
        # Convert start and end dates to datetime objects
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)

        # Calculate the difference between start and end dates in days
        delta = end_date - start_date

        # Iterate over each day between start and end dates
        dates = []
        for i in range(delta.days + 1):
            dates.append((start_date + timedelta(days=i)).isoformat())

        return dates

if __name__ == '__main__':
    example_transactions = [{'amount': -100, 'date': '2024-06-01 19:04:53.712267'},
                            {'amount': 200, 'date': '2024-06-02 19:10:53.712267'},
                            {'amount': -200, 'date': '2024-06-04 19:10:53.712267'},
                            {'amount': 300, 'date': '2024-06-06 19:10:53.712267'},
                            {'amount': -1000, 'date': '2024-06-07 19:10:53.712267'},
                            {'amount': -1000, 'date': '2024-06-07 19:15:53.712267'},
                            {'amount': -1000, 'date': '2024-06-07 19:20:53.712267'},
                            {'amount': -1000, 'date': '2024-06-08 19:25:53.712267'},
                            {'amount': -1000, 'date': '2024-06-10 19:30:53.712267'},
                            {'amount': 10000, 'date': '2024-07-12 19:10:53.712267'},
                            {'amount': -1000, 'date': '2024-07-13 19:10:53.712267'}]
    example_balances = [{'amount': 400, 'date': '2024-06-01 19:04:53.712267'},  #
                        {'amount': 400, 'date': '2024-06-02 19:04:53.712267'},
                        {'amount': 400, 'date': '2024-06-03 19:04:53.712267'},
                        {'amount': 400, 'date': '2024-06-04 19:04:53.712267'},
                        {'amount': 400, 'date': '2024-06-05 19:04:53.712267'},
                        {'amount': 400, 'date': '2024-06-06 19:04:53.712267'},  #
                        {'amount': -2900, 'date':'2024-06-07 19:04:53.712267'},  #
                        {'amount': -3900, 'date': '2024-06-08 19:04:53.712267'},  #
                        {'amount': -3900, 'date': '2024-06-09 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-10 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-11 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-12 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-13 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-14 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-15 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-16 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-17 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-18 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-19 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-20 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-21 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-22 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-23 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-24 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-25 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-26 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-27 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-28 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-29 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-06-30 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-01 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-02 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-03 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-04 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-05 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-06 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-07 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-08 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-09 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-10 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-11 19:04:53.712267'},
                        {'amount': -3900, 'date': '2024-07-12 19:04:53.712267'},  #
                        {'amount': -3100, 'date': '2024-07-13 19:04:53.712267'}]  #
    b = BalancesAndTransactions(example_transactions, example_balances)
    b.check_balances()
    for item in b.balances_with_check:
        print(item)
