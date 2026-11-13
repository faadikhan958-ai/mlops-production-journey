# Day 60 — SQLAlchemy Engine, Session & Declarative Base

**Date:** 13 November 2026  
**Sprint:** MLOps Production Engineering  
**Status:** Implementation & Verification  
**Focus:** SQLAlchemy Integration with FastAPI and PostgreSQL  
**Total Tickets:** 15

## Objective

Integrate SQLAlchemy into the existing FastAPI-based MLOps application and establish a reliable database session management architecture for PostgreSQL.

The main objective was to understand and implement database connectivity, engine management, session factories, ORM foundations, and FastAPI request-scoped database dependencies.

---

## Ticket 01 — SQLAlchemy Fundamentals

**Task:** Understand SQLAlchemy and its role in production applications.

**Implementation:**
- Studied SQLAlchemy ORM architecture.
- Understood the difference between SQLAlchemy Core and ORM.
- Learned how Python applications communicate with relational databases.
- Understood the role of SQLAlchemy in managing database operations.
- Reviewed synchronous and asynchronous database interaction.

**Key Learning:** SQLAlchemy provides a structured way to interact with relational databases using Python.

## Ticket 02 — SQLAlchemy Async Architecture

**Task:** Understand asynchronous SQLAlchemy architecture and PostgreSQL driver compatibility.

**Implementation:**
- Studied SQLAlchemy 2.x asynchronous architecture.
- Understood AsyncEngine and AsyncSession.
- Learned the role of asyncpg as an asynchronous PostgreSQL driver.
- Reviewed asynchronous database connection flow.
- Understood why synchronous and asynchronous database interfaces should not be mixed incorrectly.

**Important Concepts:**
- AsyncEngine
- AsyncSession
- asyncpg
- Async database operations
- Connection lifecycle

**Key Learning:** Asynchronous database operations help FastAPI applications handle I/O-bound workloads without unnecessarily blocking the event loop.

## Ticket 03 — Database Engine Fundamentals

**Task:** Understand SQLAlchemy Engine and its responsibilities.

**Implementation:**
- Studied how SQLAlchemy creates database engines.
- Understood database connectivity management.
- Learned the purpose of connection pooling.
- Understood why an engine should generally be created once and reused throughout the application lifecycle.
- Reviewed database engine configuration.

**Example:**

```python
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    DATABASE_URL,
    echo=False
)
```

**Key Learning:** Engine manages database connectivity and provides the foundation for creating database connections.

## Ticket 04 — Database Connection Management

**Task:** Understand how SQLAlchemy establishes communication with PostgreSQL.

**Implementation:**
- Studied the difference between Engine and Connection.
- Understood how database connections are acquired from the engine.
- Reviewed connection pooling.
- Learned the role of database URL configuration.
- Understood internal Docker networking for database connectivity.

**Key Learning:** Engine manages connectivity, while an individual connection represents an active communication channel with the database.

## Ticket 05 — SQLAlchemy Session Fundamentals

**Task:** Understand database sessions and their lifecycle.

**Implementation:**
- Studied the purpose of SQLAlchemy sessions.
- Understood how sessions execute database operations.
- Learned the difference between a connection and a session.
- Reviewed commit, rollback, and close operations.
- Understood transaction management responsibilities.

**Important Concepts:**
- Session lifecycle
- Commit
- Rollback
- Close
- Transaction management

**Key Learning:** A database session manages ORM operations and transaction state; it is not the same thing as a database connection.

## Ticket 06 — AsyncSession & Session Factory

**Task:** Understand asynchronous database sessions and reusable session factories.

**Implementation:**
- Studied AsyncSession.
- Understood async_sessionmaker.
- Learned how session factories create independent database sessions.
- Reviewed expire_on_commit configuration.
- Understood why a single AsyncSession must not be shared across concurrent requests.

**Example:**

```python
from sqlalchemy.ext.asyncio import async_sessionmaker

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)
```

**Key Learning:** A session factory provides a reusable mechanism for creating independent AsyncSession instances.

## Ticket 07 — Declarative Base & ORM Models

**Task:** Understand SQLAlchemy Declarative Base and ORM model structure.

**Implementation:**
- Studied Object Relational Mapping (ORM).
- Understood the purpose of DeclarativeBase.
- Learned how Python classes represent database tables.
- Reviewed model metadata.
- Understood how ORM models inherit from a common Base class.

**Example:**

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

**Key Learning:** Declarative Base provides a common foundation for defining SQLAlchemy ORM models and managing their metadata.

## Ticket 08 — Database Configuration Management

**Task:** Configure database connectivity using environment-based settings.

**Implementation:**
- Reviewed PostgreSQL connection configuration.
- Understood database URL structure.
- Learned the role of environment variables.
- Reviewed `.env` and `.env.example`.
- Understood Docker Compose service DNS.
- Reviewed secure credential management.

**Example:**

```text
postgresql+asyncpg://user:password@postgres:5432/mlops_db
```

**Important:** Actual credentials must remain outside version control.

**Key Learning:** Environment-based configuration separates application settings from source code and improves security and deployment flexibility.

## Ticket 09 — SQLAlchemy Engine Module

**Task:** Organize database engine configuration in a dedicated module.

**Implementation:**
- Reviewed engine initialization responsibilities.
- Understood centralized engine management.
- Reviewed asynchronous engine creation.
- Studied connection pooling configuration.
- Understood application-level engine lifecycle.

**Important Concepts:**
- create_async_engine()
- AsyncEngine
- Connection pooling
- Database URL
- Engine lifecycle

**Key Learning:** Keeping engine configuration centralized makes the database layer easier to maintain and test.

## Ticket 10 — Session Factory Module

**Task:** Establish reusable database session factory configuration.

**Implementation:**
- Reviewed async_sessionmaker configuration.
- Understood how the session factory binds to the engine.
- Studied independent session creation.
- Reviewed expire_on_commit behavior.
- Understood session lifecycle management.

**Key Learning:** Session factory separates session creation from the application routes that consume database sessions.

## Ticket 11 — Declarative Base Module

**Task:** Establish a centralized ORM foundation for future database models.

**Implementation:**
- Reviewed DeclarativeBase implementation.
- Understood common Base inheritance.
- Studied metadata registration.
- Reviewed the relationship between ORM models and database tables.
- Considered future database migration requirements.

**Key Learning:** A centralized Declarative Base provides consistent model definitions and metadata management.

## Ticket 12 — FastAPI Database Dependency

**Task:** Integrate SQLAlchemy sessions with FastAPI Dependency Injection.

**Implementation:**
- Studied FastAPI dependency injection.
- Understood the purpose of Depends().
- Learned how to provide database sessions to API routes.
- Reviewed request-scoped session management.
- Studied yield-based dependency lifecycle.

**Example:**

```python
async def get_db():
    async with SessionLocal() as session:
        yield session
```

**Usage:**

```python
db: AsyncSession = Depends(get_db)
```

**Key Learning:** FastAPI dependencies provide database sessions to routes without requiring every route to manually create and manage its own session.

## Ticket 13 — Session Lifecycle, Cleanup & Failure Testing

**Task:** Verify database session lifecycle and application behavior during database failures.

**Implementation:**
- Verified separate AsyncSession instances for independent requests.
- Tested session cleanup after request completion.
- Tested application behavior when PostgreSQL became unavailable.
- Verified controlled HTTP 503 response behavior.
- Tested exception logging using logger.exception().
- Verified database recovery after PostgreSQL became available again.
- Performed a successful database connectivity test.

**Connection Test Result:**

```text
connected 1
```

**Verification:**
- Separate session behavior: Verified.
- Session cleanup: Verified.
- Database unavailable handling: Tested.
- HTTP 503 behavior: Tested.
- Exception logging: Tested.
- Database recovery: Verified.
- Successful connection: Confirmed.

**Key Learning:** Production database integration requires proper session isolation, cleanup, failure handling, logging, and recovery—not just successful connectivity.

## Ticket 14 — LinkedIn Career Sprint & GitHub Portfolio

**Task:** Improve professional portfolio presentation for Junior AI/ML Engineer opportunities.

**Planned Activities:**
- Review LinkedIn professional profile.
- Improve project presentation.
- Organize GitHub portfolio links.
- Prepare professional project descriptions.
- Highlight relevant AI/ML and MLOps skills.

**Additional GitHub Activity:**

Worked on the ML Fundamentals repository:

Repository:
https://github.com/faadikhan958-ai/ml-fundamentals-day1-to-45

**Implementation:**
- Finalized the root README filename.
- Created `README.md`.
- Added a professional project introduction.
- Committed the README directly to the main branch.

**Commit Message:**

```text
Add root README
```

**Key Learning:** A root README provides visitors with an introduction to the repository, its purpose, and its contents.

## Ticket 15 — Documentation, Evidence & Professional Git Commit

**Task:** Document Day 60 implementation and prepare professional version control changes.

**Documentation Requirements:**
- Record SQLAlchemy architecture.
- Document engine configuration.
- Document session factory.
- Document Declarative Base.
- Explain FastAPI database dependency.
- Record database connectivity testing.
- Record failure handling and recovery evidence.
- Review project changes before committing.

**Recommended Documentation File:**

```text
notes/day-60-sqlalchemy-engine-session-base.md
```

**Git Verification:**

```powershell
git status --short
```

Review staged changes before committing.

**Recommended Professional Commit Message:**

```text
feat(database): integrate SQLAlchemy async sessions with FastAPI
```

This commit message should only be used after the corresponding implementation and documentation changes have actually been reviewed and staged.

**Security Rules:**
- Never commit `.env`.
- Never expose database passwords or API tokens.
- Never commit private PDFs or personal data.
- Avoid staging unrelated files.
- Review changes before every commit.

---

## Key Technical Learnings

1. SQLAlchemy provides an ORM layer for Python applications.
2. AsyncEngine manages asynchronous database connectivity.
3. AsyncSession manages asynchronous ORM operations.
4. async_sessionmaker creates independent database sessions.
5. DeclarativeBase provides a foundation for ORM models.
6. Engine and Session have different responsibilities.
7. Connection pooling helps reuse database connections.
8. FastAPI Dependency Injection simplifies database session management.
9. `Depends()` provides dependencies to API routes.
10. `yield` supports resource management through dependency lifecycle.
11. Each concurrent request should have its own AsyncSession.
12. Session cleanup is essential for reliable resource management.
13. Database failures should produce controlled application errors.
14. `logger.exception()` helps capture exception tracebacks.
15. Environment variables help protect sensitive database configuration.
16. Database connectivity, transaction management, and session lifecycle are separate concerns.
17. Git commits should accurately describe the changes being committed.

## Day 60 — Verification Summary

| Area | Verification |
|---|---|
| SQLAlchemy Architecture | Studied |
| AsyncEngine | Covered |
| Database Connection | Covered |
| AsyncSession | Covered |
| Session Factory | Covered |
| Declarative Base | Covered |
| Environment Configuration | Covered |
| FastAPI Dependency | Covered |
| Session Lifecycle | Verified |
| Database Failure Handling | Tested |
| HTTP 503 Behavior | Tested |
| Exception Logging | Tested |
| Database Recovery | Verified |
| GitHub Root README | Created and committed |
| Final Documentation & Git Review | Pending verification |

## Day Completion

Day 60 focused on establishing the foundation for SQLAlchemy-based PostgreSQL integration in the existing FastAPI MLOps application.

The major learning areas included asynchronous database architecture, engine and session management, ORM fundamentals, FastAPI dependency injection, request-scoped sessions, resource cleanup, and database failure recovery.

A separate GitHub portfolio improvement was also completed by creating and committing the root `README.md` in the ML Fundamentals repository.

**Next Focus:** Continue production-grade database integration by developing database models, Pydantic schemas, and structured persistence for ML prediction records.

---

**Day 60 — SQLAlchemy Engine, Session & Declarative Base**

**Learning Track:** AI/ML → MLOps Production Engineering  
**Documentation Date:** 13 November 2026