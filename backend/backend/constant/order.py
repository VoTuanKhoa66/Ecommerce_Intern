class OrderStatus():
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    PREPARING = 'preparing'
    SHIPPING = 'shipping'
    DELiVERED = 'delivered'
    CANCELLED = 'cancelled'
    RETURNED = 'returned'

    STATUS_ORDER = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (PREPARING, 'Preparing'),
        (SHIPPING, 'Shipping'),
        (DELiVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
        (RETURNED, 'Returned')
    ]
