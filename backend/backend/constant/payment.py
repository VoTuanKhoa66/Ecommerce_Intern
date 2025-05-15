class PaymentMethods():
    CASH = 'cash'
    QRCODE = 'qrcode'

    PAYMENT_METHODS = [
        (CASH, 'Cash'),
        (QRCODE, 'QRcode'),
    ]

class PaymentStatus():
    PENDING = 'pending'
    PAID = 'paid'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    EXPIRED = 'expired'

    STATUS_PAYMENTS = [
        (PENDING, 'Peding'),
        (PAID, 'Paid'),
        (CANCELLED, 'Cancelled'),
        (FAILED, 'Failed'),
        (EXPIRED, 'Expired')
    ]
