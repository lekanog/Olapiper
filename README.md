# Dukka_test
This is a Django Rest Framework-based API that allows users to automate recurring payments for items purchased on an e-commerce site. The API includes the following functionality:

Authentication system: Users can authenticate themselves to access the API.

Create Payment: Users can create recurring payments for items they have purchased on the e-commerce site.

Terminate Payment: Users can terminate their recurring payments at any time.

Payment History: Users can view their own payment history.

All History: Superusers can view the payment history for all users.

Add Card: Users can add a new card as a payment method.

History: Users can view their own card payment history.

Payment View: Users can view their personal payments.

All Payment View: Superusers can view all users' payments.


#API Endpoints
The following API endpoints are available:

POST /api/token/: Users can authenticate themselves using this endpoint. This endpoint returns an access token that can be used to authenticate subsequent requests to the API.

POST /createpayment/: Users can create a new recurring payment using this endpoint.

POST /terminate/: Users can terminate a recurring payment using this endpoint.

GET /paymenthistory/: Users can view their own payment history using this endpoint.

GET /allhistory/: Superusers can view the payment history for all users using this endpoint.

POST /add-card/: Users can add a new card as a payment method using this endpoint.

GET /history/: Users can view their own card payment history using this endpoint.

GET /paymentview/: Users can view their personal payments using this endpoint.

GET /allpaymentview/: Superusers can view all users' payments using this endpoint.

Authentication
This API uses Token Authentication. To authenticate, users should include their token in the Authorization header of their requests. The format for the Authorization header is as follows:

Authorization: Bearer <access_token>
To obtain an access token, users should send a POST request to the /api/token/ endpoint with their username and password in the request body. The response to this request will include an access token that can be used to authenticate subsequent requests.

Creating a New Payment
To create a new recurring payment, users should send a POST request to the /createpayment/ endpoint. The request body should include the following information:

item: The name of the product being purchased.

item_id: The id of the item

amount: The amount of the payment.

frequency: The frequency of the payment (e.g. monthly, weekly, yearly).

method: The id of the card being used to make the payment.( So basically you need to add a card first before processing payment)


Terminating a Payment
To terminate a recurring payment, users should send a POST request to the /terminate/ endpoint. The request body should include the following information:

payment_id: The ID of the payment that should be terminated.


Viewing Payment History
To view payment history, users should send a GET request to the /paymenthistory/ endpoint. The response to this request will include a list of all payments made by the user.

Viewing All Payment History
To view payment history for all users, superusers should send a GET request to the /allhistory/ endpoint. The response to this request will include a list of all payments made


Using this  as the url https://web-production-0269.up.railway.app/ it can be also be tested on line or on postman.
