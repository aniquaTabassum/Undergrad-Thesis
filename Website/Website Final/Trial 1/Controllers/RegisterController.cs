using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Trial_1.Models;
using System.Web.Mvc;
using System.Data;

namespace Trial_1.Controllers
{
    
    public class RegisterController : Controller
    {
        
        // GET: Register
        [HttpGet]
        public ActionResult Register()
        {
            return View(new User());
        }

        [HttpPost]
        public ActionResult Register(User user)
        {
           
            Session["user"] = user;
             return RedirectToAction("PersonalPreference", "Preference");
        }


       


    }
}