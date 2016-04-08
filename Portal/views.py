from django.shortcuts import render, render_to_response, RequestContext, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.template.context import RequestContext
from placement.models import Candidate
from placement.models import Recruiter
from placement.models import Interview
import simplejson
# Create your views here.

# call the home template
def home(request):
    return render_to_response("home.html")

# call the Single sign on/o-auth2 for candidate registration
def reg_goo(request):
    context = RequestContext(request,{'request': request,'user': request.user})
    c ={}
    c.update(csrf(request))
    return render_to_response('sample.html', c, context_instance=context)

# call the Single sign on/o-auth2 for recruiter registration
def goo(request):
    context = RequestContext(request,{'request': request,'user': request.user})
    c ={}
    c.update(csrf(request))
    return render_to_response('sample1.html', c, context_instance=context)

#candidate login
def jseek(request):
    c ={}
    context = RequestContext(request,{'request': request,'user': request.user})
    c.update(csrf(request))
    return render_to_response('login.html', c, context_instance=context)
 
# recruiter login  
def rec(request):
    context = RequestContext(request,{'request': request,'user': request.user})
    c ={}
    c.update(csrf(request))
    return render_to_response('rlogin.html', c, context_instance=context)

# recruiter authentication
def rauth(request):

    username1 = request.POST.get('username','')
    password1 = request.POST.get('password','')
    try:
        user=Recruiter.objects.get(username=username1,password=password1)
    except Recruiter.DoesNotExist:
        return render_to_response('invalid_login.html')
    else:
        r = Recruiter.objects.get(username=username1)
        response = HttpResponseRedirect('/r_login')
        response.set_cookie('rid', r.rid)
        return response

# Recruiter loggedin page call
def r_login(request):
    return render_to_response('rloggedin.html')

# candidate authentication
def jauth(request):

    username1 = request.POST.get('username','')
    password1 = request.POST.get('password','')
    try:
        user=Candidate.objects.get(username=username1,password=password1)
    except Candidate.DoesNotExist:
        return render_to_response('invalid_login.html')
    else:
        j = Candidate.objects.get(username=username1)
        return render_to_response('jloggedin.html',{'cid': j.cid, 'rank': j.rank})

# general logout
def logout(request):
    auth.logout(request)
    response = render_to_response('logout.html')
    response.delete_cookie('rid')
    return response

# Recruiter entry page
def rcheck(request):
    c ={}
    c.update(csrf(request))
    cid = request.POST.get('cid','')
    t = Candidate.objects.all().filter(cid=cid)
    context = RequestContext(request,{'list': t})
    if not(t):
        return render_to_response('nor1.html')
    else:
        return render_to_response('rprint.html', c, context_instance=context)

# candiate normal registration form
def reg(request):
    c ={}
    c.update(csrf(request))
    return render_to_response('reg.html',c)

# candidate id auto generation
def register(request):
    no = len(Candidate.objects.all())
    no1 = 'CA'
    auth.logout(request)
    if no==0:
        no = 10000 + 1
        tno = str(no)
        tno = no1 + tno
        t=Candidate(cid=tno,username=request.POST.get('username',''),password=request.POST.get('password',''),name=request.POST.get('name',''),gender=request.POST.get('gender',''),college=request.POST.get('college',''),grad=request.POST.get('grad',''),course=request.POST.get('course',''),mobile=request.POST.get('mobile',''),email=request.POST.get('email',''),city=request.POST.get('city',''),zip=request.POST.get('zip',''))
        t.save()
        return render_to_response('regs.html')
    elif no==1:
        no = 10000 + 2
        tno = str(no)
        tno = no1 + tno
        t=Candidate(cid=tno,username=request.POST.get('username',''),password=request.POST.get('password',''),name=request.POST.get('name',''),gender=request.POST.get('gender',''),college=request.POST.get('college',''),grad=request.POST.get('grad',''),course=request.POST.get('course',''),mobile=request.POST.get('mobile',''),email=request.POST.get('email',''),city=request.POST.get('city',''),zip=request.POST.get('zip',''))
        t.save()
        return render_to_response('regs.html')
    else:
        no = no + 10001
        tno = str(no)
        tno = no1 + tno
        t=Candidate(cid=tno,username=request.POST.get('username',''),password=request.POST.get('password',''),name=request.POST.get('name',''),gender=request.POST.get('gender',''),college=request.POST.get('college',''),grad=request.POST.get('grad',''),course=request.POST.get('course',''),mobile=request.POST.get('mobile',''),email=request.POST.get('email',''),city=request.POST.get('city',''),zip=request.POST.get('zip',''))
        t.save()
        return render_to_response('regs.html')

# recruiter id auto generation
def save(request):
    no = len(Recruiter.objects.all())
    no1 = 'REC'
    auth.logout(request)
    if no==0:
        no = 10000 + 1
        tno = str(no)
        tno = no1 + tno
        t=Recruiter(rid=tno,username=request.POST.get('username',''),email=request.POST.get('email',''),password=request.POST.get('password',''),name=request.POST.get('name',''))
        t.save()
        return render_to_response('recs.html')
    elif no==1:
        no = 10000 + 2
        tno = str(no)
        tno = no1 + tno
        t=Recruiter(rid=tno,username=request.POST.get('username',''),email=request.POST.get('email',''),password=request.POST.get('password',''),name=request.POST.get('name',''))
        t.save()
        return render_to_response('recs.html')
    else:
        no = no + 10001
        tno = str(no)
        tno = no1 + tno
        t=Recruiter(rid=tno,username=request.POST.get('username',''),email=request.POST.get('email',''),password=request.POST.get('password',''),name=request.POST.get('name',''))
        t.save()
        return render_to_response('recs.html')

# recruiter search candidate form 
def entry(request):
    c ={}
    c.update(csrf(request))
    return render_to_response('entry.html', c)

# mark add to candidate table
def mark(request):
    i = Interview(cid=request.POST['cid'],rid=request.COOKIES['rid'],mark=request.POST['mark'])
    i.save()
    return render_to_response('marks.html')

# report generation
def report(request):
    # Average mark generation
    t = Interview.objects.all()
    my_cid = ""
    for id in t:
        no = len(Interview.objects.all().filter(cid=id.cid))
        c = Candidate.objects.get(cid=id.cid)
        if my_cid != id.cid:
            if no == 1:
                c.mark = marks
                c.save()
                my_cid = id.cid
                marks = 0
            elif no == 2:
                marks = add(id.cid)
                c.mark = marks/2
                c.save()
                my_cid = id.cid
            elif no ==3:
                marks = add(id.cid)
                c.mark = marks/3
                c.save()
                my_cid = id.cid
    
    # Rank mark generation
    temp = Candidate.objects.all().order_by('-mark')
    no = 1
    for id in temp:
        c = Candidate.objects.get(cid=id.cid)
        c.rank = no
        no = no + 1
        c.save() 
    candidate = Candidate.objects.all().order_by('rank')
    return render_to_response('report.html',{'details': candidate})

#add the all interviewer marks
def add(cid):
    c = Interview.objects.filter(cid=cid)
    marks = 0
    for id in c:
        marks = marks + id.mark
    return marks