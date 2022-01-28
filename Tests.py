from jennie.angular import create_login_signup_project

sample_angular_project = {
  "output_dir": "Output/Folder/Path",
  "project_name": "ewiki",
  "db_type": "sqlite3",
  "tables": [
    {
      "table_name": "user",
      "columns": [
        {
          "column_name": "firstname",
          "column_type": "single_line_text"
        },
        {
          "column_name": "lastname",
          "column_type": "single_line_text"
        },
        {
          "column_name": "email",
          "column_type": "email"
        },
        {
          "column_name": "password",
          "column_type": "password"
        }
      ],
      "type": "user"
    }
  ]
}

def create_login_signup_angular(config):
    create_login_signup_project(config)

if __name__ == '__main__':
    create_login_signup_angular(sample_angular_project)