from crm.models import LeadExtend, Campaign, Lead, LandingPage

def check_key_words(lead):
    if lead.lead_extend is None:
        check = ""
    else:
        check = LeadExtend.objects.get(id=lead.lead_extend.id)
        check = check.key_word
    return check

def rodo(rodo):
    if rodo is True:
        response = "zaakceptowany"
    else:
        response = "niezaakceptowany"
    return response

def description_lead(lead):
    campaign = Campaign.objects.get(id=lead.campaign.id)
    landing_page = LandingPage.objects.get(id=lead.landing_page.id)

    description = f"""
*** ❖ Dane leada ***
`Imię:` {lead.name}
`Telefon:` {lead.phone}
`Słowo kluczowe:` {check_key_words(lead)}
`RODO:` {rodo(lead.rodo)}
`Informacja:` {lead.info}
`SMS ID:` {lead.sms_id}

*** ❖ Źródło  leada ***
`Nazwa kampanii:` {campaign.name}
`Link do landing page:` {lead.landing_page.link}
`Opis kampanii:` {landing_page.description}
"""
    return description
