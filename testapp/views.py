# from django.shortcuts import render
# Create your views here.
# from flask import Flask, render_template
# from flask import request
# import hashlib
# import hmac
# import base64
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return render_template('testapp/start.html')
#
# # secretKey = "<ENTER_YOUR_SECRETKEY_HERE>"
# secretKey = "d1cb82a1aff501aa64aa0a608d2aa8cc4e9fcc1f"
# @app.route('/request', methods=["POST"])
# def handlerequest():
#   mode = "TEST" # <-------Change to TEST for test server, PROD for production
#   postData = {
#       "appId" : request.form['appId'],
#       "orderId" : request.form['orderId'],
#       "orderAmount" : request.form['orderAmount'],
#       "orderCurrency" : request.form['orderCurrency'],
#       "orderNote" : request.form['orderNote'],
#       "customerName" : request.form['customerName'],
#       "customerPhone" : request.form['customerPhone'],
#       "customerEmail" : request.form['customerEmail'],
#       "returnUrl" : request.form['returnUrl'],
#       "notifyUrl" : request.form['notifyUrl']
#   }
#   sortedKeys = sorted(postData)
#   signatureData = ""
#   for key in sortedKeys:
#     signatureData += key+postData[key]
#   message = signatureData.encode('utf-8')
#   #get secret key from your config
#   secret = secretKey.encode('utf-8')
#   signature = base64.b64encode(hmac.new(secret,message,digestmod=hashlib.sha256).digest()).decode("utf-8")
#   if mode == 'PROD':
#     url = "https://www.cashfree.com/checkout/post/submit"
#   else:
#     url = "https://test.cashfree.com/billpay/checkout/post/submit"
#   return render_template('testapp/request.html', postData = postData,signature = signature,url = url)
#
# @app.route('/response', methods=["GET","POST"])
# def handleresponse():
#
#   postData = {
#     "orderId" : request.form['orderId'],
#     "orderAmount" : request.form['orderAmount'],
#     "referenceId" : request.form['referenceId'],
#     "txStatus" : request.form['txStatus'],
#     "paymentMode" : request.form['paymentMode'],
#     "txMsg" : request.form['txMsg'],
#     "signature" : request.form['signature'],
#     "txTime" : request.form['txTime']
#    }
#
#   signatureData = ""
#   signatureData = postData['orderId'] + postData['orderAmount'] + postData['referenceId'] + postData['txStatus'] + postData['paymentMode'] + postData['txMsg'] + postData['txTime']
#
#   message = signatureData.encode('utf-8')
#   # get secret key from your config
#   secret = secretKey.encode('utf-8')
#   computedsignature = base64.b64encode(hmac.new(secret,message,digestmod=hashlib.sha256).digest()).decode('utf-8')
#   return render_template('testapp/response.html', postData = postData,computedsignature = computedsignature)
#
# if __name__ == '__main__':
#   app.run("",5000,debug='true')
#
#
# def app(request):
#     return render(request, 'app.html')


from django.shortcuts import render,redirect
from .models import  ApplicationFormClass
from django.http import  HttpResponse
import random
import hashlib
import hmac
import base64
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import http.client
secretKey = "b9d19c24bf7698932fc193727db0f741a60e39fd "




def app(request):
    if request.method =='POST':
        number = "".join(random.sample("0123456789abcdefghijklmn", 6))
        number_id = number
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        # order = request.POST.get("orderid")
        amount = request.POST.get("amount")
        dob = request.POST.get('dob')
        board = request.POST.get('board')
        father = request.POST.get("father")
        mother = request.POST.get("mother")
        qualification = request.POST.get('qualification')
        sname = request.POST.get('sname')
        saddress = request.POST.get('Saddress')
        haddress = request.POST.get('Haddress')
        state = request.POST.get('state')
        anum = request.POST.get('anum')
        phonenum = request.POST.get('num')
        email = request.POST.get('email')
        personphoto = request.FILES.get('photo')
        signaturephoto = request.FILES.get('signature')

        number = '19'+'{:03d}'.format(random.randrange(1, 999))
        username = (state + board + qualification+ number)

        if ApplicationFormClass.objects.filter(emailID=email).exists():
            return HttpResponse('email id taken in database use another emaild')
        else:
            af = ApplicationFormClass( order_id = number_id, firstName = fname, lastName = lname, amount= amount, date_of_birth = dob, board = board, fatherName = father, motherName = mother, qualification = qualification, schoolName = sname, schoolAddress = saddress, homeAddress = haddress , aadharNumber = anum, phoneNumber = phonenum, emailID = email, personPhoto = personphoto,  signaturePhoto = signaturephoto,state = state, username = username)
            af.save()
        # return HttpResponse('data inserted sucessfull')
        postData = {
            "appId": '',
            "orderId": number_id,
            "orderAmount":amount,
            "Name": fname,
            "Phone": phonenum,
            "Email":  email,
        }
        sortedKeys = sorted(postData)
        signatureData = ""
        for key in sortedKeys:
            signatureData += key + postData[key]
        message = signatureData.encode('utf-8')
        # get secret key from your config
        secret = secretKey.encode('utf-8')
        signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest()).decode("utf-8")
        url = "https://test.cashfree.com/billpay/checkout/post/submit"
        return render('app.html', postData=postData, signature=signature, url=url)

    return render(request, 'app.html')