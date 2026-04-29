from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

report_path = "LibraryProject_Report.pdf"

doc = SimpleDocTemplate(report_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CodeBlock', fontName='Courier', fontSize=8, leading=10, spaceAfter=8))

story = []

story.append(Paragraph('Library Project Report', styles['Heading1']))
story.append(Paragraph('Generated on: April 29, 2026', styles['Normal']))
story.append(Spacer(1, 12))

story.append(Paragraph('1. Project Summary', styles['Heading2']))
story.append(Paragraph('This project implements a simple Java library management system with package organization, basic object-oriented design, exception handling, and JDBC connectivity to a MySQL database.', styles['Normal']))
story.append(Spacer(1, 8))

story.append(Paragraph('2. Project Structure', styles['Heading2']))
folder_diagram = '''LibraryProject/
├── pom.xml
├── database-setup.sql
├── mysql-connector-java-8.1.0.jar
├── Main.java
├── Main.class
├── com/
│   └── library/
│       ├── db/
│       │   └── DBConnection.java
│       ├── exception/
│       │   └── LibraryException.java
│       ├── model/
│       │   ├── Item.java
│       │   ├── Book.java
│       │   └── Member.java
│       └── service/
│           ├── LibraryService.java
│           └── JDBCLibraryService.java
└── src/
    └── main/
        └── java/
            └── com/library/...'''
story.append(Preformatted(folder_diagram, styles['CodeBlock']))
story.append(Spacer(1, 8))

story.append(Paragraph('3. Key Components', styles['Heading2']))
story.append(Paragraph('The project includes the following main components:', styles['Normal']))
story.append(Paragraph('- DB connection helper: DBConnection.java', styles['Bullet']))
story.append(Paragraph('- Custom exception: LibraryException.java', styles['Bullet']))
story.append(Paragraph('- Domain model: Item, Book, Member', styles['Bullet']))
story.append(Paragraph('- In-memory service: LibraryService.java', styles['Bullet']))
story.append(Paragraph('- Database service: JDBCLibraryService.java', styles['Bullet']))
story.append(Paragraph('- Execution entry point: Main.java', styles['Bullet']))
story.append(Spacer(1, 8))

story.append(Paragraph('4. MySQL Setup', styles['Heading2']))
story.append(Paragraph('The database schema was created using the following SQL script:', styles['Normal']))
sql_snippet = '''CREATE DATABASE IF NOT EXISTS librarydb;
USE librarydb;

CREATE TABLE IF NOT EXISTS books (
  id VARCHAR(50) PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS members (
  id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS borrowings (
  member_id VARCHAR(50),
  book_id VARCHAR(50),
  borrowed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (member_id, book_id),
  FOREIGN KEY (member_id) REFERENCES members(id),
  FOREIGN KEY (book_id) REFERENCES books(id)
);'''
story.append(Preformatted(sql_snippet, styles['CodeBlock']))
story.append(Spacer(1, 8))

story.append(Paragraph('5. JDBC Configuration', styles['Heading2']))
story.append(Paragraph('The JDBC connection helper uses the MySQL URL, username, and password as shown below.', styles['Normal']))
story.append(Preformatted('''private static final String URL = "jdbc:mysql://localhost:3306/librarydb?useSSL=false&serverTimezone=UTC";
private static final String USER = "root";
private static final String PASSWORD = "1264";''', styles['CodeBlock']))
story.append(Spacer(1, 8))

story.append(Paragraph('6. Main Application Flow', styles['Heading2']))
story.append(Paragraph('Main.java tests the database connection, then runs a simple JDBC demonstration that inserts books and members, borrows and returns a book, and lists the stored data.', styles['Normal']))
main_snippet = '''JDBCLibraryService library = new JDBCLibraryService();

Book book1 = new Book("1", "Java Basics", "Author A");
Book book2 = new Book("2", "Advanced Java", "Author B");
library.addBook(book1);
library.addBook(book2);

Member member1 = new Member("1", "John Doe");
library.registerMember(member1);

library.borrowBook("1", "1");
library.returnBook("1", "1");
'Books in the database:'
library.listAllBooks().forEach(System.out::println);
'Members in the database:'
library.listAllMembers().forEach(System.out::println);'''
story.append(Preformatted(main_snippet, styles['CodeBlock']))
story.append(Spacer(1, 8))

story.append(Paragraph('7. Test Result', styles['Heading2']))
story.append(Paragraph('The project was run successfully in terminal and confirmed JDBC connectivity with the MySQL database. The output showed successful connection, book borrow/return, and database row retrieval.', styles['Normal']))
story.append(Spacer(1, 8))

story.append(Paragraph('8. Notes', styles['Heading2']))
story.append(Paragraph('This project can run without Maven by using the downloaded JDBC driver JAR and the command line, so XML build configuration is optional.', styles['Normal']))
story.append(Spacer(1, 8))

story.append(Paragraph('Run command:', styles['Heading2']))
story.append(Preformatted('java -cp .;mysql-connector-java-8.1.0.jar Main', styles['CodeBlock']))


doc.build(story)
print(f"Generated PDF: {report_path}")
