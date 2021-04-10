using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Trial_1.Models;

namespace Trial_1.Controllers
{
    public class QuestionController : Controller
    {
        int id = 0;
        int count = 0;
        // GET: Question
        [HttpGet]
        public ActionResult AskQuestions()
        {
            Questions questions = new Questions();
            questions.check = "true";
            selectQuestion(questions.questionLevel, questions.levelMap);
            return View(questions);
        }

        [HttpPost]
        public ActionResult AskQuestions(Questions questions)
        {
            postAnswerToDb(questions);
            return RedirectToAction("Thanks", "Home");
        }


        public void postAnswerToDb(Questions questions)
        {
            id = (int)System.Web.HttpContext.Current.Session["id"];
            count = (int)System.Web.HttpContext.Current.Session["count"];
            count += 1;
            User user = (User)System.Web.HttpContext.Current.Session["user"];
            PreferenceDecider preferenceDecider = (PreferenceDecider)System.Web.HttpContext.Current.Session["preference"];
            String query = "INSERT INTO ANSWERS VALUES("+id+", '"+user.gender+"', '"+user.ageRange+"', '"+user.occupation+"', '"+user.fieldOfStudy+"', '"+user.hometown+"', '"+user.maritalStatus+"', '"+user.spouseMoveStatus+"', '"+user.spouceEmployment+"', "+preferenceDecider.avgRent+", "+preferenceDecider.homeTown+", "+preferenceDecider.schooling+", "+preferenceDecider.spouceStatus+", "+preferenceDecider.security+", "+questions.q1Satisfaction+", "+questions.q2Satisfaction+", "+questions.q3Satisfaction+", DEFAULT)";
            DatabaseModel databaseModel = new DatabaseModel();
            databaseModel.insert(query);
           
            String query2 = "UPDATE QUESTION_BANK SET USAGE_COUNT = " + count + " WHERE SET_NUM = " + id;

            databaseModel = new DatabaseModel();
            databaseModel.update(query2);
        }
        public void selectQuestion(List<String> questionLevel, Dictionary<String, String> levelMap)
        {
            string query = "SELECT * FROM QUESTION_BANK ORDER BY USAGE_COUNT ASC";
            
            int questionId = 0;
            DataSet dataSet = new DataSet();
            DatabaseModel databaseModel = new DatabaseModel();
            dataSet = databaseModel.selectFunction(query);
            
            if (dataSet.Tables[0].Rows.Count > 0)
            {
                questionId = (int)dataSet.Tables[0].Rows[0].ItemArray[0];
                Session["id"] = questionId;
                Session["count"] = (int)dataSet.Tables[0].Rows[0].ItemArray[13];
                
                for (int i = 1; i< 13; i++)
                {
                    questionLevel.Add(levelMap[dataSet.Tables[0].Rows[0].ItemArray[i].ToString()]);
                }
            }
           
        }
    }
}