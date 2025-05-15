import requests
import uuid
import hashlib
import hmac
from decouple import config

def create_momo_payment(order):
    endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"

    order_id = f"{order.id}"
    request_id = f"{order.id}-{uuid.uuid4().hex[:4]}"
    amount = int(order.total_price)
    phone = f"{order.user.phone}"
    partner_code = config("MOMO_PARTNER_CODE")
    access_key = config("MOMO_ACCESS_KEY")
    secret_key = config("MOMO_SECRET_KEY")
    redirect_url = "https://yourdomain.com/thank-you"
    ipn_url = "https://yourdomain.com/api/momo/ipn"
    order_info = f"Thanh toan don hang #{order.id}-{phone}"
    request_type = "captureWallet"
    extra_data = ""

    raw_signature = f"accessKey={access_key}&amount={amount}&extraData={extra_data}&ipnUrl={ipn_url}&orderId={order_id}&orderInfo={order_info}&partnerCode={partner_code}&redirectUrl={redirect_url}&requestId={request_id}&requestType={request_type}"
    signature = hmac.new(secret_key.encode(), raw_signature.encode(), hashlib.sha256).hexdigest()

    payload = {
        "partnerCode": partner_code,
        "accessKey": access_key,
        "requestId": request_id,
        "amount": str(amount),
        "orderId": order_id,
        "orderInfo": order_info,
        "redirectUrl": redirect_url,
        "ipnUrl": ipn_url,
        "extraData": extra_data,
        "requestType": request_type,
        "signature": signature,
        "lang": "vi"
    }

    response = requests.post(endpoint, json=payload)
    return response.json()
