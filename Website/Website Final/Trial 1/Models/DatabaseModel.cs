using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace Trial_1.Models
{
    public class DatabaseModel
    {
 
            string connectionString = ConfigurationManager.ConnectionStrings["myConnectionString"].ConnectionString;
        DataSet dataset { get; set; }
            public DataSet selectFunction(string command)
            {
                dataset = new DataSet();

                using (SqlConnection sqlConnection = new SqlConnection(connectionString))
                {
                    sqlConnection.Open();
                    SqlDataAdapter sqlDataAdapter = new SqlDataAdapter(command, sqlConnection);
                    sqlDataAdapter.Fill(dataset);
                    return dataset;


                }
            }

            public void update(string query)
            {
                using (SqlConnection sqlConnection = new SqlConnection(connectionString))
                {
                    sqlConnection.Open();
                    SqlCommand sqlCommand = new SqlCommand(query, sqlConnection);
                    sqlCommand.ExecuteNonQuery();
                }

            }

            public void insert(string query)
            {
                using (SqlConnection sqlConnection = new SqlConnection(connectionString))
                {
                    sqlConnection.Open();
                    SqlCommand sqlCommand = new SqlCommand(query, sqlConnection);
                    sqlCommand.ExecuteNonQuery();
                }

            }
        }
    }
