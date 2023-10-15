from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

# Create your views here.
def home(request):

    # Check if the user is authenticated
    if request.user.is_authenticated:

        # Access user attributes
        email = request.user.email
        full_name = request.user.get_full_name()
        short_name = request.user.get_short_name()

        # You can also access any custom fields you've added to your custom user model
        # custom_field = request.user.custom_field

        # Perform actions based on user details
        print(f"Email: {email}")
        print(f"Full Name: {full_name}")
        print(f"Short Name: {short_name}")
        # print(f"Custom Field: {custom_field}")
    else:
        # Handle the case when the user is not authenticated
        pass


    #_______________________________ Email for first time registering users ___________________________________
    # subject = 'Welcome to NyayConnect - Your Legal Services Marketplace'
    # message = '''

    # Dear''', full_name,

    # '''Welcome to NyayConnect, your one-stop destination for legal services in India!

    # We're excited to have you on board as a member of our platform. Whether you're seeking legal advice, looking for experienced lawyers, or offering legal services, NyayConnect is here to simplify your journey.

    # Here's what you can expect from NyayConnect:

    # 1. **Find Legal Experts**: Explore a wide network of experienced legal professionals and firms who can assist you with your specific legal needs.

    # 2. **Secure and Convenient**: Our platform is designed with your security and convenience in mind. Your information is safe with us, and our user-friendly interface makes it easy to navigate.

    # 3. **Personalized Recommendations**: We use advanced algorithms to provide personalized recommendations, ensuring that you connect with the right legal experts for your unique requirements.

    # 4. **Stay Informed**: Access valuable legal resources, articles, and updates to stay informed about the latest legal developments in India.

    # 5. **24/7 Support**: Our support team is available around the clock to assist you with any questions or concerns you may have.

    # To get started, simply log in to your NyayConnect account using the credentials you provided during registration. If you haven't completed your profile yet, we encourage you to do so to maximize your experience on our platform.

    # Ready to embark on your legal journey? [Login now](#) and explore the possibilities with NyayConnect.

    # If you ever need assistance or have any questions, feel free to reach out to our support team at support@nyayconnect.com. We're here to help!

    # Thank you for choosing NyayConnect. We look forward to serving your legal needs and making your journey through the legal landscape a seamless one.

    # Warm regards,

    # Team, NyayConnect'''

    # from_email = 'youremail@gmail.com'
    # recipient_list = ['discoverfreshmen@gmail.com','abhisheksingh2022@vitbhopal.ac.in']

    # send_mail(subject, message, from_email, recipient_list)

    # ______________________________________ email body ends here _____________________________________

    return render(request, 'index.html')



def logout_view(request):
    logout(request)
    return redirect('/')