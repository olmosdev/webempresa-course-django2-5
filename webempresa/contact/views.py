from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST) # To render the template again with the same info submitted if the form was not validated properly
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")

            # If everything went well, we redirect
            # It's a good practice to let Django resolve the URLs itself
            email = EmailMessage(
                "La Caffettiera: New contact message", # Email Subject
                "From {} <{}>\n\nWrote:\n\n{}".format(name, email, content), # Body or Content
                "no-reply@inbox.live.smtp.mailtrap.io", # Source mail
                ["olmos.develop@gmail.com"], # Destination mail
                reply_to=[email] # Email to reply
            )
            try:
                email.send()
                return redirect(reverse("contact") + "?ok") # Similar to the emplate tag "url"
            except:
                import traceback
                traceback.print_exc()
                # An error has occurred
                return redirect(reverse("contact") + "?fail") # Similar to the emplate tag "url"

    return render(request, "contact/contact.html", {"form": contact_form})
