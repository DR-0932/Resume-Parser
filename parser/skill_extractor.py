import re

SKILL_SET = {
    # Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript", "go", "golang",
    "rust", "php", "ruby", "kotlin", "swift", "scala", "r", "matlab",
    "perl", "bash", "shell scripting", "powershell", "objective-c",
    "dart", "groovy", "haskell", "lua", "fortran", "cobol", "assembly",

    # Web – Frontend
    "html", "html5", "css", "css3", "sass", "scss", "less",
    "bootstrap", "tailwind css", "material ui", "chakra ui",
    "react", "reactjs", "next.js", "nextjs", "vue", "vuejs",
    "angular", "angularjs", "svelte", "jquery",

    # Web – Backend
    "nodejs", "express", "expressjs", "nestjs",
    "flask", "django", "fastapi", "tornado",
    "spring", "spring boot", "hibernate",
    "laravel", "codeigniter", "symfony",
    "rails", "ruby on rails",
    "asp.net", "asp.net core",

    # APIs & Communication
    "rest", "rest api", "restful api", "graphql",
    "grpc", "soap", "web sockets", "webhooks",

    # Databases – SQL
    "sql", "mysql", "postgresql", "postgres", "oracle",
    "sql server", "mssql", "sqlite", "mariadb",

    # Databases – NoSQL
    "mongodb", "redis", "cassandra", "couchdb",
    "dynamodb", "firebase", "firestore", "neo4j",

    # Data Science / ML / AI
    "machine learning", "deep learning", "artificial intelligence",
    "nlp", "natural language processing", "computer vision",
    "data science", "predictive modeling",
    "pandas", "numpy", "scipy",
    "scikit-learn", "sklearn",
    "tensorflow", "keras", "pytorch",
    "xgboost", "lightgbm", "catboost",
    "opencv", "spacy", "nltk",
    "huggingface", "transformers",

    # Big Data
    "hadoop", "spark", "pyspark", "kafka",
    "hive", "pig", "flink", "airflow",

    # Data & Analytics
    "data analysis", "data analytics",
    "data visualization", "business intelligence",
    "power bi", "tableau", "looker", "qlik",
    "excel", "microsoft excel", "google sheets",

    # Cloud Platforms
    "aws", "amazon web services", "azure", "microsoft azure",
    "gcp", "google cloud platform",
    "ec2", "s3", "lambda", "rds", "cloudformation",
    "firebase hosting", "vercel", "netlify",

    # DevOps & Infrastructure
    "docker", "docker compose", "kubernetes", "helm",
    "terraform", "ansible", "chef", "puppet",
    "ci/cd", "jenkins", "github actions", "gitlab ci",
    "circleci", "travis ci",

    # Version Control
    "git", "github", "gitlab", "bitbucket", "svn",

    # Operating Systems
    "linux", "unix", "ubuntu", "centos",
    "windows", "macos",

    # Mobile Development
    "android", "android development", "ios", "ios development",
    "flutter", "react native", "xamarin",

    # Testing & QA
    "unit testing", "integration testing", "system testing",
    "pytest", "junit", "testng", "jest", "mocha", "chai",
    "selenium", "cypress", "playwright",

    # Security
    "cyber security", "information security",
    "jwt", "oauth", "oauth2", "saml",
    "authentication", "authorization",
    "bcrypt", "hashing", "encryption",
    "penetration testing", "vapt",

    # Software Architecture
    "system design", "low level design", "high level design",
    "microservices",
}

def extract_skills(text: str):
  if not text:
      return []

  text = text.lower()
  text = text.replace(",", " ").replace("/", " ").replace("(", " ").replace(")", " ")

  found = set()
  for skill in SKILL_SET:
      if skill in text:
          found.add(skill)

  return sorted(found)
