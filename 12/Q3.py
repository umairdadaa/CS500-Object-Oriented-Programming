from abc import ABC,abstractmethod
# Target Interface
class PayPalPaymentGateway(ABC):
    @abstractmethod
    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
        pass
# Adaptee
class LegacyPaymentGateway:
    def process_credit_card_payment(self, credit_card_number: str, expiration_date: str, cvv: str, amount: float) -> bool:
        print("Simulates processing a credit card payment")

# Adapter
class PaypalAdapter(PayPalPaymentGateway):
    def __init__(self, obj: LegacyPaymentGateway) -> None:
        self.__obj = obj
    
    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
        credit_card_number = self.get_credit_card_number(email_address)
        expiration_date = self.get_expiration_date(email_address)
        cvv=self.get_cvv(email_address)
        return self.__obj.process_credit_card_payment(credit_card_number, expiration_date, cvv, amount)
    
    def get_credit_card_number(self,email_address)->str:
        return "1234567890123456"
    
    def get_expiration_date(self,email_address)->str:
        return "08/27"
    def get_cvv(self,email_address)-> str:
        return "123"
    
class PaymentGatewayFactory:
    @staticmethod
    def get_payment_gateway()-> PayPalPaymentGateway:
        return PaypalAdapter(LegacyPaymentGateway())
    
def main():
    payment_gateway = PaymentGatewayFactory().get_payment_gateway()
    payment_gateway.process_paypal_payment("peter@yahoo.com",10000)

if __name__ == "__main__":
    main()