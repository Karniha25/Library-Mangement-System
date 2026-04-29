# Library Management Project

This is a simple Java library management system with JDBC support for MySQL.

## Project Structure

- `Main.java` - application entry point
- `src/main/java/com/library/db/DBConnection.java` - JDBC connection helper
- `src/main/java/com/library/exception/LibraryException.java` - custom exception
- `src/main/java/com/library/model/Item.java` - base item class
- `src/main/java/com/library/model/Book.java` - book model
- `src/main/java/com/library/model/Member.java` - member model
- `src/main/java/com/library/service/LibraryService.java` - in-memory service example
- `src/main/java/com/library/service/JDBCLibraryService.java` - database-backed service
- `database-setup.sql` - MySQL schema setup script
- `pom.xml` - Maven build file with MySQL JDBC dependency

## Setup

1. Install Java 11 or later.
2. Install MySQL and run the server.
3. Run `database-setup.sql` in MySQL Workbench.
4. Update `src/main/java/com/library/db/DBConnection.java` with your MySQL username and password.

## Run

### With Maven

```cmd
cd c:\Users\sharo\OneDrive\Desktop\LibraryProject
mvn compile
mvn exec:java -Dexec.mainClass="Main"
```

### Without Maven

```cmd
cd c:\Users\sharo\OneDrive\Desktop\LibraryProject
javac -cp mysql-connector-java-8.1.0.jar -d . src/main/java/**/*.java
java -cp .;mysql-connector-java-8.1.0.jar Main
```

## Notes

- `mysql-connector-java-8.1.0.jar` is used as the JDBC driver.
- `pom.xml` includes the MySQL JDBC dependency.
- The application currently demonstrates adding books, registering a member, borrowing and returning a book, and listing stored data.
