using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Trial_1.Models;

namespace Trial_1.Controllers
{
    public class PreferenceController : Controller
    {
        
        // GET: Preference
        [HttpGet]
        public ActionResult PersonalPreference()
        {
            return View(new PreferenceDecider());
        }

        [HttpPost]
        public ActionResult PersonalPreference(PreferenceDecider pf)
        {
            Session["preference"] = pf;

            return RedirectToAction("AskQuestions", "Question");
        }


        
    }
}