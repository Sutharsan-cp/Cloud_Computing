class CurrencyConverterService:
    def convert_to_rupees(self, amount):
        conversion_rate = 74.0  # Example conversion rate
        return amount * conversion_rate

    def convert_to_dollars(self, amount):
        conversion_rate = 1 / 74.0  # Example conversion rate
        return amount * conversion_rate