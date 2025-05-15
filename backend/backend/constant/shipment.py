class ShipmentStatus():
    PENDING = 'pending'
    Processing = 'processing'
    SHIPPING = 'shipping'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'
    RETURNED = 'returned'

    STATUS_SHIPMENT = [
        (PENDING, 'Pending'),
        (SHIPPING, 'Shipping'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
        (RETURNED, 'Returned')
    ]
