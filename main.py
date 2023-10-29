from fastapi import FastAPI, Request , Form
#from fastapi.security.csrf import CSRFRequest
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from DataBase.database import Session
#from model import User, Result
#from schemas import Result
import model
import schemas
from chat_gpt import prompting
from promptin import question_prompt, ans_prompt
import threading
from sound_recording import record_audio_to_wav
from fastapi.security.csrf import CSRFProtect


app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")
csrf = CSRFProtect(app)

@app.get('/',response_class=HTMLResponse)
async def read_item(request:Request):
    return templates.TemplateResponse('login.html',{'request':request})

@app.post("/result")
async def result(id:int ,res:schemas.Result):
    db = Session()
    new_data = model.Result(coding_lang = res.coding_lang,
                            filler_words = res.filler_words,
                            grammer = res.grammer,
                            result = res.result,
                            user_id = id)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@app.post("/signup", response_class=HTMLResponse)
async def user_signup(request: Request, name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    db = Session()
    new_data = model.User(
                          name = name,
                          email = email,
                          password = password)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return templates.TemplateResponse("signup_success.html", {"request": request, "user": new_data})



@app.post('/interview')
async def interview_ai(lange : str,exp: str | None , company :str | None):
    prompt_question = question_prompt(lange, exp, company)
    question_by_chatGPT = prompting(prompt_question)
    question_in_list = question_by_chatGPT.split(';')
    for i in question_in_list:
        print(i)
        #if 1==1:
            #text = record_audio_to_wav()
            #print(text)
            #result_thread = threading.Thread(target=ans_prompt, args=(i,text,))
            #result_thread.start()
    





























