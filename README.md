**Agentic HR Hiring Planner**

**An agentic AI application that helps HR professionals plan a startup hiring process.
Example input:**

I need to hire a founding engineer and a GenAI intern. Can you help?

The agent will then:

Ask clarifying questions such as budget, skills, timeline, and location

Suggest job description drafts

Create a hiring checklist or plan

Present results in structured Markdown or JSON

Provide supporting artifacts like a draft approval email and simulated search results

**Features**

Multi-step reasoning using LangGraph with the following flow: intake → clarify → plan_roles → draft_jd → checklist → tools → finalize

Clarifying questions to collect missing information

Job Descriptions generated in Markdown and JSON formats

Hiring checklists with week-by-week tasks

Tool integrations including simulated Google search, email writer, and checklist builder

Memory with file-based session persistence

Analytics saved as a CSV log of session runs

Two frontends available:

Command Line Interface (CLI)

Streamlit web application

**Architecture**

The application runs a sequence of steps through a LangGraph workflow:

Intake – parse the request

Clarify – ask questions such as budget, skills, and location

Plan Roles – build structured role specifications

Draft JD – generate job descriptions

Checklist – produce a week-by-week hiring plan

Tools – simulate search results and create an approval email

Finalize – produce artifacts such as final_markdown and final_json

**Project Structure**

config.py – model and default configuration

memory.py – session persistence and analytics logging

prompts.py – system prompt and clarifying questions

run_cli.py – CLI entrypoint

schemas.py – Pydantic models for RoleSpec, JD, Checklist, and State

streamlit_app.py – Streamlit web application

tools.py – simulated tools for search, email, and checklist

requirements.txt – Python dependencies

graph/graph.py – defines the LangGraph pipeline
