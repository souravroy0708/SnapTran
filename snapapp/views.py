# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_auth,logout
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import json
from datetime import datetime, timedelta,date
import socket
#import espeak
import time
import urllib, json
import  subprocess

def text_to_speech(request):
    """
    Convert text to speech
    """
    text = request.GET.get('q','')
    to_lang = request.GET.get('target','')
    form_lang = request.GET.get('source','')
    msg = None
    converted_text = None 
    if text and form_lang and to_lang :
        #URL url=new URL(parentUrl+"key="+apiKey+"&q="+encodedText+"&target="+languageTo+"&source="+languageFrom);
	#String apiKey="AIzaSyAaSZmcHV9aEkY9sjHmrZxuc2F7Qm2Khgw";
	URL="https://www.googleapis.com/language/translate/v2?key=AIzaSyAaSZmcHV9aEkY9sjHmrZxuc2F7Qm2Khgw&q=%s&target=%s&\
                              source=%s" %(text,to_lang,form_lang)
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
        converted_text = data['data']['translations'][0]['translatedText']
    else:
        msg = "text,form_lang,to_lang annot be blank"
    #print "text ",text,"form_lang ",form_lang,"to_lang ",to_lang,"converted_text ",converted_text
    if converted_text:
        #currenttimestamp = int(time.time())
        #import pdb;pdb.set_trace()
        #file_path = "speech_%s.wav" %(str(currenttimestamp))
        #print "file_path  ---- ",file_path ,converted_text
        
        #espeak -kn -stdout converted_text -w  kani2324.w
        #subprocess.call("espeak -kn -stdout "+converted_text+" -w kan23234324.w",shell=True) 
        #subprocess.call("espeak  -"+ to_lang+" -stdout "+ converted_text,shell=True)
        #subprocess.call('espeak -'+to_lang+' -stdout "'+ converted_text +'"',shell=True)

        subprocess.call('espeak "'+ converted_text +'"',shell=True) 
       # speech_path = file_path
    else:
        #speech_path = "None"
        msg = "Nothing to convert"

    print "converted_text",converted_text
    #try:
    #        converted_text = converted_text.decode("UTF-8")
    #except:
    #        converted_text = "None"

    return_object = {"msg":msg,"converted_text":converted_text}
    return_object_final = {"result":return_object}
    return HttpResponse(json.dumps(return_object_final),
            content_type="application/json")
    

def index(request):
    """
    Gender Prediction index page
    """
    text = None
    converted_text = None
    if request.method == "POST":
        print "POST method"
        text = request.POST.get('text_from','')
    	to_lang = request.POST.get('target','')
    	form_lang = request.POST.get('source','')
    	msg = None
    	converted_text = None
    	if text and form_lang and to_lang :
        	#URL url=new URL(parentUrl+"key="+apiKey+"&q="+encodedText+"&target="+languageTo+"&source="+languageFrom);
        	#String apiKey="AIzaSyAaSZmcHV9aEkY9sjHmrZxuc2F7Qm2Khgw";
        	URL="https://www.googleapis.com/language/translate/v2?key=AIzaSyAaSZmcHV9aEkY9sjHmrZxuc2F7Qm2Khgw&q=%s&target=%s&\
                              source=%s" %(text,to_lang,form_lang)
        	response = urllib.urlopen(URL)
        	data = json.loads(response.read())
        	converted_text = data['data']['translations'][0]['translatedText']
    	else:
        	msg = "text,form_lang,to_lang annot be blank"
    	print "text ",text,"form_lang ",form_lang,"to_lang ",to_lang,"converted_text ",converted_text
    	if converted_text:
        	#currenttimestamp = int(time.time())
        	#import pdb;pdb.set_trace()
        	#file_path = "speech_%s.wav" %(str(currenttimestamp))
        	#print "file_path  ---- ",file_path ,converted_text
        
        	#espeak -kn -stdout converted_text -w  kani2324.w
        	#subprocess.call("espeak -kn -stdout "+converted_text+" -w kan23234324.w",shell=True) 
        	#subprocess.call("espeak  -"+ to_lang+" -stdout "+ converted_text,shell=True)
        	#subprocess.call('espeak -'+to_lang+' -stdout "'+ converted_text +'"',shell=True)

        	subprocess.call('espeak "'+ converted_text +'"',shell=True)
       	# speech_path = file_path
    	else:
        	#speech_path = "None"
        	msg = "Nothing to convert"
        #try:
        #    converted_text = converted_text.decode("UTF-8")
        #except:
        #    converted_text = "None"
        #converted_text = "Your text has been played"
    else:
        print "GET method"

    return render(request, 'index.html',{"text":text,"converted_text":converted_text,"to_lang":to_lang,"form_lang":form_lang})  

      
