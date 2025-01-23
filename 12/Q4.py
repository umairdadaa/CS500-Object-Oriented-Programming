from abc import ABC, abstractmethod

# LegacyNotificationSystem class
class LegacyNotificationSystem:
    def send_sms_notification(self, phone_number: str, message: str) -> None:
        print(f"Simulates sending an SMS notification to {phone_number}: {message}")

# NewNotificationSystem interface
class NewNotificationSystem(ABC):
    @abstractmethod
    def send_email_notification(self, email_address: str, subject: str, body: str) -> None:
        pass

    @abstractmethod
    def send_push_notification(self, device_token: str, title: str, message: str) -> None:
        pass

    @abstractmethod
    def send_social_media_update(self, social_media_platform: str, post_content: str) -> None:
        pass

# NotificationAdapter class
class NotificationAdapter(NewNotificationSystem):
    def __init__(self, legacy_system: LegacyNotificationSystem) -> None:
        self.__legacy_system = legacy_system

    def send_email_notification(self, email_address: str, subject: str, body: str) -> None:
        # Simulating email notification using SMS
        message = f"Subject: {subject}\nBody: {body}"
        self.__legacy_system.send_sms_notification(email_address, message)

    def send_push_notification(self, device_token: str, title: str, message: str) -> None:
        # Simulating push notification using SMS
        combined_message = f"Title: {title}\nMessage: {message}"
        self.__legacy_system.send_sms_notification(device_token, combined_message)

    def send_social_media_update(self, social_media_platform: str, post_content: str) -> None:
        # Simulating social media update using SMS
        social_message = f"Posting on {social_media_platform}: {post_content}"
        self.__legacy_system.send_sms_notification("Social Media Platform", social_message)

# Example usage
def main():
    # Legacy system instance
    legacy_system = LegacyNotificationSystem()

    # Adapter instance
    adapter = NotificationAdapter(legacy_system)

    # Using the adapter to send different types of notifications
    adapter.send_email_notification("user@example.com", "Important Update", "Please check your email for details.")
    adapter.send_push_notification("device_token_12345", "New Message", "You have a new push notification!")
    adapter.send_social_media_update("Twitter", "Check out our latest post on Twitter!")

if __name__ == "__main__":
    main()
