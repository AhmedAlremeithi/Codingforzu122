# classes.py

class Guest:
    """Represents a hotel guest."""
    def __init__(self, name, contact_info, email, account_id):
        # Protected and private attributes
        self._name = name
        self._contact_info = contact_info
        self._email = email
        self.__account_id = account_id
        self._reservation_history = []  # List of Booking objects

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getContactInfo(self):
        return self._contact_info

    def setContactInfo(self, contact_info):
        self._contact_info = contact_info

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getAccountId(self):
        return self.__account_id

    def setAccountId(self, account_id):
        self.__account_id = account_id

    def getReservationHistory(self):
        return self._reservation_history

    def setReservationHistory(self, reservation_history):
        self._reservation_history = reservation_history

    def addBooking(self, booking):
        # Add a booking to the guest's reservation history
        self._reservation_history.append(booking)

    def __str__(self):
        return "Guest: " + self._name


class LoyaltyGuest(Guest):
    """Represents a loyal guest with reward points."""
    def __init__(self, name, contact_info, email, account_id, loyalty_points, reward_level):
        super().__init__(name, contact_info, email, account_id)
        self.__loyalty_points = loyalty_points
        self.__reward_level = reward_level

    def getLoyaltyPoints(self):
        return self.__loyalty_points

    def setLoyaltyPoints(self, loyalty_points):
        self.__loyalty_points = loyalty_points

    def getRewardLevel(self):
        return self.__reward_level

    def setRewardLevel(self, reward_level):
        self.__reward_level = reward_level

    def redeemPoints(self, points):
        # Redeem loyalty points
        if self.__loyalty_points >= points:
            self.__loyalty_points -= points

    def __str__(self):
        return "Loyalty Guest: " + self.getName()


class Room:
    """Represents a hotel room."""
    def __init__(self, room_number, room_type, amenities, price_per_night, is_available):
        self._room_number = room_number
        self._room_type = room_type
        self._amenities = amenities  # List
        self._price_per_night = price_per_night
        self.__is_available = is_available

    def getRoomNumber(self):
        return self._room_number

    def setRoomNumber(self, room_number):
        self._room_number = room_number

    def getRoomType(self):
        return self._room_type

    def setRoomType(self, room_type):
        self._room_type = room_type

    def getAmenities(self):
        return self._amenities

    def setAmenities(self, amenities):
        self._amenities = amenities

    def getPrice(self):
        return self._price_per_night

    def setPrice(self, price):
        self._price_per_night = price

    def getAvailability(self):
        return self.__is_available

    def setAvailability(self, status):
        self.__is_available = status

    def listAmenities(self):
        # Return list of amenities
        return self._amenities

    def __str__(self):
        return "Room: " + self._room_number


class Booking:
    """Represents a hotel booking."""
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        self.__booking_id = booking_id
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date

    def getBookingId(self):
        return self.__booking_id

    def setBookingId(self, booking_id):
        self.__booking_id = booking_id

    def getGuest(self):
        return self._guest

    def setGuest(self, guest):
        self._guest = guest

    def getRoom(self):
        return self._room

    def setRoom(self, room):
        self._room = room

    def getCheckInDate(self):
        return self._check_in_date

    def setCheckInDate(self, date):
        self._check_in_date = date

    def getCheckOutDate(self):
        return self._check_out_date

    def setCheckOutDate(self, date):
        self._check_out_date = date

    def confirmBooking(self):
        return "Booking Confirmed"

    def cancelBooking(self):
        return "Booking Cancelled"

    def __str__(self):
        return "Booking ID: " + self.__booking_id


class Invoice:
    """Represents an invoice for a booking."""
    def __init__(self, invoice_id, booking, room_charges, service_fees, total):
        self.__invoice_id = invoice_id
        self._booking = booking
        self._room_charges = room_charges
        self._service_fees = service_fees
        self.__total = total

    def getInvoiceId(self):
        return self.__invoice_id

    def setInvoiceId(self, invoice_id):
        self.__invoice_id = invoice_id

    def getBooking(self):
        return self._booking

    def setBooking(self, booking):
        self._booking = booking

    def getRoomCharges(self):
        return self._room_charges

    def setRoomCharges(self, room_charges):
        self._room_charges = room_charges

    def getServiceFees(self):
        return self._service_fees

    def setServiceFees(self, fees):
        self._service_fees = fees

    def getTotal(self):
        return self.__total

    def setTotal(self, total):
        self.__total = total

    def calculateTotal(self):
        self.__total = self._room_charges + self._service_fees
        return self.__total

    def __str__(self):
        return "Invoice ID: " + self.__invoice_id


class Payment:
    """Represents a payment made for an invoice."""
    def __init__(self, payment_id, invoice, payment_method, amount_paid, payment_date):
        self.__payment_id = payment_id
        self._invoice = invoice
        self._payment_method = payment_method
        self._amount_paid = amount_paid
        self._payment_date = payment_date

    def getPaymentId(self):
        return self.__payment_id

    def setPaymentId(self, payment_id):
        self.__payment_id = payment_id

    def getInvoice(self):
        return self._invoice

    def setInvoice(self, invoice):
        self._invoice = invoice

    def getPaymentMethod(self):
        return self._payment_method

    def setPaymentMethod(self, method):
        self._payment_method = method

    def getAmountPaid(self):
        return self._amount_paid

    def setAmountPaid(self, amount):
        self._amount_paid = amount

    def getPaymentDate(self):
        return self._payment_date

    def setPaymentDate(self, date):
        self._payment_date = date

    def validatePayment(self):
        # Check if payment is sufficient
        return self._amount_paid >= self._invoice.getTotal()

    def __str__(self):
        return "Payment ID: " + self.__payment_id


class ServiceRequest:
    """Represents a service request made by a guest."""
    def __init__(self, request_id, guest, service_type, status):
        self.__request_id = request_id
        self._guest = guest
        self._service_type = service_type
        self._status = status

    def getRequestId(self):
        return self.__request_id

    def setRequestId(self, request_id):
        self.__request_id = request_id

    def getGuest(self):
        return self._guest

    def setGuest(self, guest):
        self._guest = guest

    def getServiceType(self):
        return self._service_type

    def setServiceType(self, service_type):
        self._service_type = service_type

    def getStatus(self):
        return self._status

    def setStatus(self, status):
        self._status = status

    def updateStatus(self, status):
        # Update request status
        self._status = status

    def __str__(self):
        return "Service Request ID: " + self.__request_id



class Feedback:
    """Represents feedback provided by a guest after their stay."""
    def __init__(self, feedback_id, guest, rating, comments, submission_date):
        self.__feedback_id = feedback_id
        self._guest = guest
        self._rating = rating
        self._comments = comments
        self._submission_date = submission_date

    def getFeedbackId(self):
        return self.__feedback_id

    def setFeedbackId(self, feedback_id):
        self.__feedback_id = feedback_id

    def getGuest(self):
        return self._guest

    def setGuest(self, guest):
        self._guest = guest

    def getRating(self):
        return self._rating

    def setRating(self, rating):
        self._rating = rating

    def getComments(self):
        return self._comments

    def setComments(self, comments):
        self._comments = comments

    def getSubmissionDate(self):
        return self._submission_date

    def setSubmissionDate(self, date):
        self._submission_date = date

    def summarizeFeedback(self):
        # Return the feedback summary as a string
        return "Rating: " + str(self._rating) + ", Comment: " + self._comments

    def __str__(self):
        return "Feedback ID: " + self.__feedback_id
