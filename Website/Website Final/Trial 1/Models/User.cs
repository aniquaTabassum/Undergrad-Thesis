using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Web;
using System.Web.Mvc;

namespace Trial_1.Models
{

    public class User
    {
        public User()
        {
            File = new List<HttpPostedFileBase>();

        }
        public int userid { get; set; }


        [Required(ErrorMessage ="Required")]
        [Display(Name = "Gender")]
        public string gender { get; set; }

        [Required(ErrorMessage = "Required")]
        [Display(Name = "Age Range")]
        public string ageRange { get; set; }

        [Required(ErrorMessage = "Required")]
        [Display(Name = "Occupation")]
        public string occupation { get; set; }

        [Required(ErrorMessage = "Required")]
        [Display(Name = "Field of Study")]
        public string fieldOfStudy { get; set; }


        [Required(ErrorMessage = "Required")]

        [Display(Name = "Hometown")]
        public string hometown { get; set; }

        [Required(ErrorMessage = "Required")]
        [Display(Name = "Marital Status")]
        public string maritalStatus { get; set; }

        [Required(ErrorMessage = "Required")]
        [Display(Name = "If your spouse is a working person, are they willing to move with you? ")]
        public string spouseMoveStatus { get; set; }

        [Required(ErrorMessage = "Required")]
        [Display(Name = "If your spouse is a working person, what is his/her occupation?")]
        public string spouceEmployment { get; set; }
        public int isAdmin { get; set; }
        public List<HttpPostedFileBase> File { get; set; }
        public string paths { get; set; }
    }

    
}
public enum Gender
{
    Male,
    Female
}
