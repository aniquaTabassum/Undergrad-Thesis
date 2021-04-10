using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Trial_1.Models
{
    public class PreferenceDecider
    {
        [Required(ErrorMessage ="Required")]
        public string avgRent { get; set; }

        [Required(ErrorMessage = "Required")]
        public string homeTown { get; set; }

        [Required(ErrorMessage = "Required")]
        public string schooling { get; set; }
        [Required(ErrorMessage = "Required")]
        public string spouceStatus { get; set; }
        [Required(ErrorMessage = "Required")]
        public string security { get; set; }

    }
}