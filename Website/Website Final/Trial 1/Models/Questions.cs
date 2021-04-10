using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Trial_1.Models
{
    public class Questions
    {
        public Questions()
        {
            levelMap.Add("1", "low");
            levelMap.Add("2", "medium");
            levelMap.Add("3", "high");
            progressbarMap.Add("low", "33.33%");
            progressbarMap.Add("medium", "66.66%");
            progressbarMap.Add("high", "100%");
        }
        [Required]
        public string q1Satisfaction { get; set; }
        [Required]
        public string q2Satisfaction { get; set; }
        [Required]
        public string q3Satisfaction { get; set; }
        public string check { get; set; }
        public Dictionary<String, String> levelMap = new Dictionary<string, string>();
        public List<String> questionLevel = new List<string>();
        public Dictionary<String, String> progressbarMap = new Dictionary<string, string>();

    }
}