import phonenumbers
from number import numbers

textExtract= phonenumbers.PhoneNumberMatcher(numbers, "IN")
for text in numbers:
    print(textExtract)


from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(numbers,"CH")
print("Country: ",geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(numbers, "RO")
print("Service Provider: ",carrier.name_for_number(service_number, "en"))

from phonenumbers import timezone
timez= phonenumbers.parse(numbers, "TZ")
print("Time Zone: ",timezone.time_zones_for_number(timez))