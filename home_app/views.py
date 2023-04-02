from django.shortcuts import render

from . models import Info, Logo, MainText, Social
from about_app.models import About, Ability, AbilityInfo, OverView
from resume_app.models import Education, Experience
from contact_app.models import Message

info = Info.objects.all().first
main_text = MainText.objects.all()
social = Social.objects.all().first
logo = Logo.objects.all().first

about = About.objects.all().first
ability = Ability.objects.all()
abilityinfo = AbilityInfo.objects.all()
overview = OverView.objects.all().first

education = Education.objects.all()
experience = Experience.objects.all()


def main_page(request):

    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    message = request.POST.get("message")

    if name and email and phone and message:

        Message.objects.create(
            name= name,
            email= email,
            phone= phone,
            message= message
        )

    return render(
        request,
        "home_app/index.html",
        {
        "info": info,
        "main_texts": main_text,
        "socials": social,
        "about": about,
        "abilitys": ability,
        "abilityinfos": abilityinfo,
        "educations": education,
        "experiences": experience,
        "overviews": overview,
        "logos": logo
        }
    )
