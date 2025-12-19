import unittest
import os
import uml_generator

class TestUMLGenerator(unittest.TestCase):

    def test_stubbed_generation(self):
        """
        Tests that the generate function returns the stubbed response
        when UML_GENERATOR_MODE is set to 'test'.
        """
        # Set the environment variable for test mode
        os.environ['UML_GENERATOR_MODE'] = 'test'

        # Call the generate function
        prompt = "This prompt will be ignored by the stub"
        plantuml_code = uml_generator.generate(prompt)

        # Check that the output is the expected stubbed response
        expected_code = """
@startuml
title Complex System UML Example

package "User Management" {
  class User {
    +id: int
    +name: string
    +email: string
    +login()
    +logout()
  }

  class Admin {
    +roleLevel: int
    +banUser(u: User)
  }

  User <|-- Admin
}

package "Product Catalog" {
  class Product {
    +id: int
    +title: string
    +price: float
    +getPriceWithTax()
  }

  class Category {
    +id: int
    +name: string
  }

  Category "1" -- "*" Product
}

package "Order System" {
  class Order {
    +id: int
    +total: float
    +checkout()
  }

  class OrderItem {
    +id: int
    +unitPrice: float
    +quantity: int
  }

  Order "1" -- "*" OrderItem
  Product "1" -- "*" OrderItem
}

package "Payment Service" {
  interface PaymentGateway {
    +makePayment(amount: float)
  }

  class RazorpayGateway {
    +makePayment(amount: float)
  }

  class PaypalGateway {
    +makePayment(amount: float)
  }

  PaymentGateway <|.. RazorpayGateway
  PaymentGateway <|.. PaypalGateway
}

User "1" -- "*" Order
Order "1" --> "1" PaymentGateway

@enduml
"""
        self.assertEqual(plantuml_code, expected_code)

        # Unset the environment variable to avoid affecting other tests
        del os.environ['UML_GENERATOR_MODE']

if __name__ == '__main__':
    unittest.main()
