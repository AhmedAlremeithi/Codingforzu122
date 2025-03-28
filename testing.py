# testing.py

from classes import Guest, LoyaltyGuest, Room, Booking, Invoice, Payment, ServiceRequest, Feedback

# Guest Account Creation
print("--- Guest Account Creation ---")
guest1 = Guest("Ahmed Alremeithi", "0509999999", "ahmed@email.com", "G001")
guest2 = LoyaltyGuest("Ghanem Alremeithi", "0508888888", "ghanem@email.com", "G002", 150, "Gold")
print(guest1)
print(guest2)

# Searching for Available Rooms
print("\n--- Searching for Available Rooms ---")
room1 = Room("101", "Single", ["Wi-Fi", "TV"], 300, True)
room2 = Room("102", "Double", ["Wi-Fi", "Mini-Bar"], 500, False)
room3 = Room("103", "Suite", ["Wi-Fi", "TV", "Jacuzzi"], 800, True)

available_rooms = []
for room in [room1, room2, room3]:
    if room.getAvailability():
        available_rooms.append(room)

for room in available_rooms:
    print("Available Room:", room.getRoomNumber(), "Type:", room.getRoomType(), "Amenities:", room.listAmenities())

# Making a Room Reservation
print("\n--- Making a Room Reservation ---")
booking1 = Booking("B001", guest1, room1, "2025-04-01", "2025-04-05")
booking2 = Booking("B002", guest2, room3, "2025-04-10", "2025-04-15")
guest1.addBooking(booking1)
guest2.addBooking(booking2)
print(booking1.confirmBooking())
print(booking2.confirmBooking())

# Booking Confirmation Notification (simulated with print)
print("\n--- Booking Confirmation Notification ---")
print("Confirmation sent to:", guest1.getEmail())
print("Confirmation sent to:", guest2.getEmail())

# Invoice Generation for a Booking
print("\n--- Invoice Generation ---")
invoice1 = Invoice("I001", booking1, room1.getPrice() * 4, 50, 0)
invoice2 = Invoice("I002", booking2, room3.getPrice() * 5, 100, 0)
print("Total for Invoice 1:", invoice1.calculateTotal())
print("Total for Invoice 2:", invoice2.calculateTotal())

# Processing Different Payment Methods
print("\n--- Payment Processing ---")
payment1 = Payment("P001", invoice1, "Credit Card", 1250, "2025-04-01")
payment2 = Payment("P002", invoice2, "Mobile Wallet", 4100, "2025-04-10")
print("Payment 1 valid:", payment1.validatePayment())
print("Payment 2 valid:", payment2.validatePayment())

# Displaying Reservation History
print("\n--- Reservation History ---")
for booking in guest1.getReservationHistory():
    print("Guest 1 Booking:", booking.getBookingId(), "Room:", booking.getRoom().getRoomNumber())

for booking in guest2.getReservationHistory():
    print("Guest 2 Booking:", booking.getBookingId(), "Room:", booking.getRoom().getRoomNumber())

# Cancellation of a Reservation
print("\n--- Cancel Reservation ---")
print("Before cancellation, Room 103 availability:", room3.getAvailability())
room3.setAvailability(True)
print(booking2.cancelBooking())
print("After cancellation, Room 103 availability:", room3.getAvailability())

# Service Request Test
print("\n--- Service Request Test ---")
request1 = ServiceRequest("SR001", guest1, "Housekeeping", "Pending")
request2 = ServiceRequest("SR002", guest2, "Room Service", "Pending")
print("Request 1 status:", request1.getStatus())
request1.updateStatus("Completed")
print("Request 1 new status:", request1.getStatus())
print("Request 2 status:", request2.getStatus())

# Feedback and Reviews
print("\n--- Feedback and Reviews ---")
feedback1 = Feedback("F001", guest1, 5, "Amazing service and clean room!", "2025-04-06")
feedback2 = Feedback("F002", guest2, 4, "Comfortable stay, but room service was slow.", "2025-04-16")
print("Feedback 1 Summary:", feedback1.summarizeFeedback())
print("Feedback 2 Summary:", feedback2.summarizeFeedback())
