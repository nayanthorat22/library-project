"""
Book Catalog Data
Realistic collection of popular Indian novels, English novels, and essential domain books.
Organized with verified ISBNs, realistic publication years, sensible stock, and accurate descriptions.
"""

BOOKS_COLLECTION = [
    # ==========================================
    # 1. INDIAN NOVELS & LITERATURE (17 Books)
    # ==========================================
    {
        "title": "The Guide",
        "author": "R. K. Narayan",
        "isbn": "9788185986074",
        "category": "Indian Novels",
        "publication_year": 1958,
        "total_copies": 4,
        "description": "The story of Raju, a corrupt tour guide who undergoes an unexpected transformation into a revered spiritual guide in the fictional town of Malgudi."
    },
    {
        "title": "Malgudi Days",
        "author": "R. K. Narayan",
        "isbn": "9788185986173",
        "category": "Indian Novels",
        "publication_year": 1943,
        "total_copies": 5,
        "description": "A delightful collection of thirty-two short stories portraying the everyday life, humors, and dilemmas of the residents of the timeless South Indian town of Malgudi."
    },
    {
        "title": "The White Tiger",
        "author": "Aravind Adiga",
        "isbn": "9781416562603",
        "category": "Indian Novels",
        "publication_year": 2008,
        "total_copies": 4,
        "description": "Winner of the Man Booker Prize 2008, this darkly comic novel follows Balram Halwai's journey from a poor village driver to a successful entrepreneur in modern Bangalore."
    },
    {
        "title": "The God of Small Things",
        "author": "Arundhati Roy",
        "isbn": "9780812979657",
        "category": "Indian Novels",
        "publication_year": 1997,
        "total_copies": 4,
        "description": "Set in Kerala, this Booker Prize-winning novel explores how childhood experiences shape two fraternal twins amid rigid social rules that dictate who should be loved."
    },
    {
        "title": "A Suitable Boy",
        "author": "Vikram Seth",
        "isbn": "9780060786526",
        "category": "Indian Novels",
        "publication_year": 1993,
        "total_copies": 3,
        "description": "A sweeping post-independence Indian epic centered on Mrs. Rupa Mehra's quest to arrange a suitable marriage for her younger daughter Lata among four extended families."
    },
    {
        "title": "Train to Pakistan",
        "author": "Khushwant Singh",
        "isbn": "9780143065883",
        "category": "Indian Novels",
        "publication_year": 1956,
        "total_copies": 4,
        "description": "A historical novel recounting the partition of India in 1947 through the tragic lens of Mano Majra, a quiet border village thrust into communal chaos."
    },
    {
        "title": "Midnight's Children",
        "author": "Salman Rushdie",
        "isbn": "9780812976533",
        "category": "Indian Novels",
        "publication_year": 1981,
        "total_copies": 3,
        "description": "A masterpiece of magical realism following Saleem Sinai, born at the stroke of midnight on August 15, 1947, whose life telepathically connects with modern India's history."
    },
    {
        "title": "The Palace of Illusions",
        "author": "Chitra Banerjee Divakaruni",
        "isbn": "9781400096206",
        "category": "Indian Novels",
        "publication_year": 2008,
        "total_copies": 4,
        "description": "A reimagining of the world-famous Indian epic Mahabharata narrated from the powerful, intimate perspective of Panchaali (Draupadi)."
    },
    {
        "title": "The Immortals of Meluha",
        "author": "Amish Tripathi",
        "isbn": "9789380658742",
        "category": "Indian Novels",
        "publication_year": 2010,
        "total_copies": 5,
        "description": "The first book in the bestselling Shiva Trilogy, presenting the legendary Tibetan immigrant Shiva as he arrives in the near-perfect empire of Meluha."
    },
    {
        "title": "The Shiva Trilogy: The Secret of the Nagas",
        "author": "Amish Tripathi",
        "isbn": "9789381626344",
        "category": "Indian Novels",
        "publication_year": 2011,
        "total_copies": 4,
        "description": "The second installment of the Shiva Trilogy follows the Neelkanth on a perilous journey across the land of India to confront the sinister Naga warrior clan."
    },
    {
        "title": "Five Point Someone",
        "author": "Chetan Bhagat",
        "isbn": "9788129135490",
        "category": "Indian Novels",
        "publication_year": 2004,
        "total_copies": 4,
        "description": "A humorous coming-of-age story following three friends navigating high academic pressures, strict grading systems, and romances at IIT Delhi."
    },
    {
        "title": "2 States: The Story of My Marriage",
        "author": "Chetan Bhagat",
        "isbn": "9788129135520",
        "category": "Indian Novels",
        "publication_year": 2009,
        "total_copies": 4,
        "description": "A romantic comedy chronicling the turbulent path to marriage of Krish (a Punjabi boy) and Ananya (a Tamil Brahmin girl) seeking parental approval."
    },
    {
        "title": "The Namesake",
        "author": "Jhumpa Lahiri",
        "isbn": "9780618485222",
        "category": "Indian Novels",
        "publication_year": 2003,
        "total_copies": 4,
        "description": "A poignant portrait of an immigrant Bengali family settling in the United States and the generational conflicts faced by their American-born son, Gogol Ganguli."
    },
    {
        "title": "The Blue Umbrella",
        "author": "Ruskin Bond",
        "isbn": "9788171673407",
        "category": "Indian Novels",
        "publication_year": 1980,
        "total_copies": 5,
        "description": "A heartwarming novella set in a Garhwal hill village about young Binya, who trades her leopard-claw pendant for a dazzling bright blue silk umbrella."
    },
    {
        "title": "The Room on the Roof",
        "author": "Ruskin Bond",
        "isbn": "9780140103663",
        "category": "Indian Novels",
        "publication_year": 1956,
        "total_copies": 4,
        "description": "Written when Ruskin Bond was just seventeen, this award-winning debut follows Rusty, an orphaned Anglo-Indian boy who runs away to discover Indian friendships and life."
    },
    {
        "title": "Godaan",
        "author": "Munshi Premchand",
        "isbn": "9788170280125",
        "category": "Indian Novels",
        "publication_year": 1936,
        "total_copies": 4,
        "description": "One of the greatest Hindi realist novels depicting the harsh economic struggle, caste oppression, and rural resilience of peasant farmer Hori."
    },
    {
        "title": "Gitanjali",
        "author": "Rabindranath Tagore",
        "isbn": "9788171676644",
        "category": "Indian Novels",
        "publication_year": 1910,
        "total_copies": 4,
        "description": "A Nobel Prize-winning collection of spiritual, devotional poems reflecting human love, nature, and communion with the divine."
    },

    # ==========================================
    # 2. POPULAR ENGLISH NOVELS (20 Books)
    # ==========================================
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling",
        "isbn": "9780747532743",
        "category": "English Novels",
        "publication_year": 1997,
        "total_copies": 5,
        "description": "The first magical adventure in which an orphan boy discovers on his eleventh birthday that he is a wizard and attends Hogwarts School of Witchcraft and Wizardry."
    },
    {
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J. K. Rowling",
        "isbn": "9780747538486",
        "category": "English Novels",
        "publication_year": 1998,
        "total_copies": 5,
        "description": "In Harry's second year at Hogwarts, whispers on castle walls announce that the Chamber of Secrets has been opened, unleashing petrifying horrors upon students."
    },
    {
        "title": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "isbn": "9780547928227",
        "category": "English Novels",
        "publication_year": 1937,
        "total_copies": 4,
        "description": "Bilbo Baggins, a quiet hobbit, is whisked away on an unexpected quest by Gandalf and thirteen dwarves to reclaim their lost kingdom from Smaug the dragon."
    },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "author": "J. R. R. Tolkien",
        "isbn": "9780544003415",
        "category": "English Novels",
        "publication_year": 1954,
        "total_copies": 4,
        "description": "Frodo Baggins inherits the One Ring of power and embarks on an epic voyage across Middle-earth towards Mount Doom to destroy it."
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "isbn": "9780141439518",
        "category": "English Novels",
        "publication_year": 1813,
        "total_copies": 5,
        "description": "A brilliant romantic social comedy tracing the witty Elizabeth Bennet and the arrogant Mr. Darcy as they overcome prejudices to find genuine respect."
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "9780060935467",
        "category": "English Novels",
        "publication_year": 1960,
        "total_copies": 4,
        "description": "Scout Finch narrates childhood in the American South as her lawyer father, Atticus Finch, defends an innocent Black man accused of a terrible crime."
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "isbn": "9780743273565",
        "category": "English Novels",
        "publication_year": 1925,
        "total_copies": 4,
        "description": "A definitive chronicle of the Jazz Age exploring Jay Gatsby's obsessive quest for Daisy Buchanan and the disillusionment of the American Dream."
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "isbn": "9780451524935",
        "category": "English Novels",
        "publication_year": 1949,
        "total_copies": 5,
        "description": "A chilling dystopian vision of a totalitarian superstate ruled by Big Brother, where thoughtcrime is outlawed and surveillance is omnipresent."
    },
    {
        "title": "Animal Farm",
        "author": "George Orwell",
        "isbn": "9780451526342",
        "category": "English Novels",
        "publication_year": 1945,
        "total_copies": 5,
        "description": "A classic political satire in which farm animals overthrow their human master only to find themselves under the tyranny of power-hungry pigs."
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "isbn": "9780062315007",
        "category": "English Novels",
        "publication_year": 1988,
        "total_copies": 5,
        "description": "An inspiring fable about Santiago, an Andalusian shepherd boy who journeys across the desert to Egypt in search of worldly treasure and his Personal Legend."
    },
    {
        "title": "The Book Thief",
        "author": "Markus Zusak",
        "isbn": "9780375842207",
        "category": "English Novels",
        "publication_year": 2005,
        "total_copies": 4,
        "description": "Narrated by Death, this unforgettable story follows young Liesel Meminger living in Nazi Germany who discovers the sustaining solace of stolen books."
    },
    {
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "isbn": "9781594631931",
        "category": "English Novels",
        "publication_year": 2003,
        "total_copies": 4,
        "description": "An unforgettable, heartbreaking story of the unlikely friendship between Amir and Hassan against the backdrop of war-torn Afghanistan."
    },
    {
        "title": "The Fault in Our Stars",
        "author": "John Green",
        "isbn": "9780525478812",
        "category": "English Novels",
        "publication_year": 2012,
        "total_copies": 4,
        "description": "A deeply moving romantic novel about Hazel Grace Lancaster and Augustus Waters, two teenagers who meet and fall in love at a cancer support group."
    },
    {
        "title": "Little Women",
        "author": "Louisa May Alcott",
        "isbn": "9780147514011",
        "category": "English Novels",
        "publication_year": 1868,
        "total_copies": 4,
        "description": "The enduring story of the four March sisters—Meg, Jo, Beth, and Amy—growing up in New England during and after the American Civil War."
    },
    {
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "isbn": "9780141441146",
        "category": "English Novels",
        "publication_year": 1847,
        "total_copies": 4,
        "description": "A courageous, plain governess falls in love with the brooding Mr. Rochester at Thornfield Hall, uncovering dark and dangerous secrets."
    },
    {
        "title": "Wuthering Heights",
        "author": "Emily Brontë",
        "isbn": "9780141439556",
        "category": "English Novels",
        "publication_year": 1847,
        "total_copies": 4,
        "description": "A passionate, turbulent tale of love, revenge, and obsession between Heathcliff and Catherine Earnshaw across the bleak Yorkshire moors."
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J. D. Salinger",
        "isbn": "9780316769488",
        "category": "English Novels",
        "publication_year": 1951,
        "total_copies": 4,
        "description": "The quintessential novel of teenage alienation following Holden Caulfield after his expulsion from prep school as he wanders New York City."
    },
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "isbn": "9780439023481",
        "category": "English Novels",
        "publication_year": 2008,
        "total_copies": 4,
        "description": "In a post-apocalyptic Panem, sixteen-year-old Katniss Everdeen volunteers to take her sister's place in a televised fight-to-the-death tournament."
    },
    {
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "isbn": "9781250301696",
        "category": "English Novels",
        "publication_year": 2019,
        "total_copies": 4,
        "description": "A psychological thriller about Alicia Berenson, a painter who shoots her husband five times and then never speaks another word."
    },
    {
        "title": "The Midnight Library",
        "author": "Matt Haig",
        "isbn": "9780525559474",
        "category": "English Novels",
        "publication_year": 2020,
        "total_copies": 4,
        "description": "Between life and death there is a library where every book gives you a chance to try another life you could have lived and undo your past regrets."
    },

    # ==========================================
    # 3. SCIENCE FICTION & FANTASY (4 Books)
    # ==========================================
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "isbn": "9780441013593",
        "category": "Science Fiction & Fantasy",
        "publication_year": 1965,
        "total_copies": 4,
        "description": "Set on the harsh desert planet Arrakis, this sci-fi epic follows young Paul Atreides as his family accepts stewardship of the galaxy's spice supply."
    },
    {
        "title": "Foundation",
        "author": "Isaac Asimov",
        "isbn": "9780553293357",
        "category": "Science Fiction & Fantasy",
        "publication_year": 1951,
        "total_copies": 4,
        "description": "Hari Seldon uses psychohistory to predict the fall of the Galactic Empire and creates a Foundation to preserve human knowledge and shorten the dark ages."
    },
    {
        "title": "Neuromancer",
        "author": "William Gibson",
        "isbn": "9780441569595",
        "category": "Science Fiction & Fantasy",
        "publication_year": 1984,
        "total_copies": 3,
        "description": "The seminal cyberpunk novel introducing cyberspace, artificial intelligence, and Case, a washed-up computer hacker hired for a high-stakes digital heist."
    },
    {
        "title": "The Name of the Wind",
        "author": "Patrick Rothfuss",
        "isbn": "9780756404741",
        "category": "Science Fiction & Fantasy",
        "publication_year": 2007,
        "total_copies": 3,
        "description": "The riveting first-person tale of Kvothe, an infamous wizard, musician, and legend recounting his tragic youth, university days, and adventures."
    },

    # ==========================================
    # 4. MYSTERY & THRILLER (4 Books)
    # ==========================================
    {
        "title": "And Then There Were None",
        "author": "Agatha Christie",
        "isbn": "9780062073488",
        "category": "Mystery & Thriller",
        "publication_year": 1939,
        "total_copies": 5,
        "description": "Ten strangers are lured to an isolated island off Devon and mysteriously killed off one by one in accordance with an eerie nursery rhyme."
    },
    {
        "title": "The Adventures of Sherlock Holmes",
        "author": "Arthur Conan Doyle",
        "isbn": "9780140437713",
        "category": "Mystery & Thriller",
        "publication_year": 1892,
        "total_copies": 4,
        "description": "Twelve of the finest investigative cases featuring the world's most famous consulting detective, Sherlock Holmes, and his companion Dr. John Watson."
    },
    {
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "isbn": "9780307474278",
        "category": "Mystery & Thriller",
        "publication_year": 2003,
        "total_copies": 4,
        "description": "Symbologist Robert Langdon investigates an intricate murder inside the Louvre, uncovering historical codes hidden in Leonardo da Vinci's artwork."
    },
    {
        "title": "Gone Girl",
        "author": "Gillian Flynn",
        "isbn": "9780307588371",
        "category": "Mystery & Thriller",
        "publication_year": 2012,
        "total_copies": 4,
        "description": "On their fifth wedding anniversary, Amy Dunne vanishes under suspicious circumstances, casting intense national media scrutiny on her husband Nick."
    },

    # ==========================================
    # 5. ROMANCE (3 Books)
    # ==========================================
    {
        "title": "Me Before You",
        "author": "Jojo Moyes",
        "isbn": "9780143124542",
        "category": "Romance",
        "publication_year": 2012,
        "total_copies": 4,
        "description": "Louisa Clark takes a job caring for Will Traynor, a wealthy young man wheelchair-bound after an accident, beginning a romance that alters both their worlds."
    },
    {
        "title": "The Notebook",
        "author": "Nicholas Sparks",
        "isbn": "9780446605236",
        "category": "Romance",
        "publication_year": 1996,
        "total_copies": 4,
        "description": "A tender love story in coastal North Carolina between Noah Calhoun and Allie Nelson, spanning social boundaries, war, and lifelong devotion."
    },
    {
        "title": "Normal People",
        "author": "Sally Rooney",
        "isbn": "9781984822178",
        "category": "Romance",
        "publication_year": 2018,
        "total_copies": 4,
        "description": "An intimate exploration of the magnetic bond and changing dynamics between Marianne and Connell through high school and university in Dublin."
    },

    # ==========================================
    # 6. CLASSIC LITERATURE (4 Books)
    # ==========================================
    {
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "isbn": "9780140449136",
        "category": "Classic Literature",
        "publication_year": 1866,
        "total_copies": 4,
        "description": "Raskolnikov, an impoverished ex-student in St. Petersburg, commits murder to test his theory of superior individuals, spiraling into guilt and redemption."
    },
    {
        "title": "The Count of Monte Cristo",
        "author": "Alexandre Dumas",
        "isbn": "9780140449266",
        "category": "Classic Literature",
        "publication_year": 1844,
        "total_copies": 4,
        "description": "Wrongfully imprisoned Edmond Dantès escapes from the Château d'If, acquires a fortune, and orchestrates an elaborate retribution against his betrayers."
    },
    {
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "isbn": "9780142437247",
        "category": "Classic Literature",
        "publication_year": 1851,
        "total_copies": 3,
        "description": "Ishmael recounts Captain Ahab's monomaniacal voyage aboard the Pequod seeking vengeance on the colossal white whale that destroyed his leg."
    },
    {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "isbn": "9781400079988",
        "category": "Classic Literature",
        "publication_year": 1869,
        "total_copies": 3,
        "description": "Tolstoy's epic panorama tracing five aristocratic Russian families through the dramatic impact of Napoleon's invasion and changing social orders."
    },

    # ==========================================
    # 7. BIOGRAPHY & AUTOBIOGRAPHY (4 Books)
    # ==========================================
    {
        "title": "Wings of Fire: An Autobiography",
        "author": "A. P. J. Abdul Kalam, Arun Tiwari",
        "isbn": "9788173711466",
        "category": "Biography & Autobiography",
        "publication_year": 1999,
        "total_copies": 5,
        "description": "The uplifting life story of Dr. A.P.J. Abdul Kalam, rising from modest origins in Rameswaram to leading India's space and missile development."
    },
    {
        "title": "The Story of My Experiments with Truth",
        "author": "Mahatma Gandhi",
        "isbn": "9788172290085",
        "category": "Biography & Autobiography",
        "publication_year": 1927,
        "total_copies": 4,
        "description": "Mahatma Gandhi's autobiographical reflection detailing his early life, spiritual principles, experiments with vegetarianism, and the genesis of Satyagraha."
    },
    {
        "title": "Steve Jobs",
        "author": "Walter Isaacson",
        "isbn": "9781451648539",
        "category": "Biography & Autobiography",
        "publication_year": 2011,
        "total_copies": 4,
        "description": "Based on over forty interviews conducted with Steve Jobs, this definitive biography charts the perfectionism and visionary drive behind Apple's revolutions."
    },
    {
        "title": "Long Walk to Freedom",
        "author": "Nelson Mandela",
        "isbn": "9780316548182",
        "category": "Biography & Autobiography",
        "publication_year": 1994,
        "total_copies": 4,
        "description": "Nelson Mandela's stirring account of his struggle against apartheid, 27 years of imprisonment on Robben Island, and historic presidency of South Africa."
    },

    # ==========================================
    # 8. SELF-HELP & PERSONAL DEVELOPMENT (5 Books)
    # ==========================================
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "isbn": "9780735211292",
        "category": "Self-Help & Development",
        "publication_year": 2018,
        "total_copies": 5,
        "description": "A practical guide teaching how small changes can produce remarkable results through habit stacking, environmental design, and continuous improvement."
    },
    {
        "title": "The Psychology of Money",
        "author": "Morgan Housel",
        "isbn": "9789390166268",
        "category": "Self-Help & Development",
        "publication_year": 2020,
        "total_copies": 5,
        "description": "Nineteen short stories exploring the strange ways people think about money, demonstrating that doing well with money is more about behavior than math."
    },
    {
        "title": "Deep Work: Rules for Focused Success in a Distracted World",
        "author": "Cal Newport",
        "isbn": "9781455586691",
        "category": "Self-Help & Development",
        "publication_year": 2016,
        "total_copies": 4,
        "description": "An argument for the superpower of deep, distraction-free concentration in cognitive professions, providing concrete strategies to cultivate it."
    },
    {
        "title": "Ikigai: The Japanese Secret to a Long and Happy Life",
        "author": "Héctor García, Francesc Miralles",
        "isbn": "9780143130727",
        "category": "Self-Help & Development",
        "publication_year": 2016,
        "total_copies": 5,
        "description": "Discover the art of finding your life's intersection of passion, mission, vocation, and profession inspired by the centenarians of Okinawa."
    },
    {
        "title": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "isbn": "9780374533557",
        "category": "Self-Help & Development",
        "publication_year": 2011,
        "total_copies": 4,
        "description": "Nobel laureate Daniel Kahneman explains the two cognitive systems that drive the way we think: System 1 (fast, intuitive) and System 2 (slow, analytical)."
    },

    # ==========================================
    # 9. COMPUTER SCIENCE & PROGRAMMING (5 Books)
    # ==========================================
    {
        "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "author": "Robert C. Martin",
        "isbn": "9780132350884",
        "category": "Computer Science & Programming",
        "publication_year": 2008,
        "total_copies": 5,
        "description": "A foundational software engineering manual filled with practical principles for writing, refactoring, and maintaining readable, robust code."
    },
    {
        "title": "The Pragmatic Programmer: Your Journey to Mastery",
        "author": "David Thomas, Andrew Hunt",
        "isbn": "9780135957059",
        "category": "Computer Science & Programming",
        "publication_year": 2019,
        "total_copies": 4,
        "description": "Timeless advice on software development craft, engineering discipline, career advancement, and avoiding common architectural pitfalls."
    },
    {
        "title": "Design Patterns: Elements of Reusable Object-Oriented Software",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "isbn": "9780201633610",
        "category": "Computer Science & Programming",
        "publication_year": 1994,
        "total_copies": 4,
        "description": "The seminal 'Gang of Four' guide cataloging twenty-three classic reusable object-oriented design patterns across creational, structural, and behavioral domains."
    },
    {
        "title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann",
        "isbn": "9781449373320",
        "category": "Computer Science & Programming",
        "publication_year": 2017,
        "total_copies": 4,
        "description": "An indispensable treatise on distributed storage systems, replication, partitioning, consensus, and batch/stream processing for modern cloud applications."
    },
    {
        "title": "Flask Web Development: Developing Web Applications with Python",
        "author": "Miguel Grinberg",
        "isbn": "9781491991732",
        "category": "Computer Science & Programming",
        "publication_year": 2018,
        "total_copies": 4,
        "description": "A hands-on, practical guide to developing production-ready web backends, databases, templates, and RESTful APIs using Flask and Python."
    },

    # ==========================================
    # 10. AI & MACHINE LEARNING (4 Books)
    # ==========================================
    {
        "title": "Artificial Intelligence: A Modern Approach (4th Edition)",
        "author": "Stuart Russell, Peter Norvig",
        "isbn": "9780134610993",
        "category": "Artificial Intelligence & ML",
        "publication_year": 2020,
        "total_copies": 4,
        "description": "The most widely referenced AI textbook worldwide, exploring intelligent agents, search algorithms, probabilistic reasoning, machine learning, and ethics."
    },
    {
        "title": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
        "author": "Aurélien Géron",
        "isbn": "9781492032649",
        "category": "Artificial Intelligence & ML",
        "publication_year": 2019,
        "total_copies": 4,
        "description": "A concrete, code-centric guide using real Python examples to train classifiers, neural networks, computer vision, and NLP architectures."
    },
    {
        "title": "Deep Learning",
        "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville",
        "isbn": "9780262035613",
        "category": "Artificial Intelligence & ML",
        "publication_year": 2016,
        "total_copies": 3,
        "description": "The definitive theoretical textbook on deep learning covering linear algebra, backpropagation, convolutional networks, and generative modeling."
    },
    {
        "title": "Pattern Recognition and Machine Learning",
        "author": "Christopher M. Bishop",
        "isbn": "9780387310732",
        "category": "Artificial Intelligence & ML",
        "publication_year": 2006,
        "total_copies": 3,
        "description": "A mathematically rigorous introduction to Bayesian probabilistic methods and inference in machine learning and pattern classification."
    },

    # ==========================================
    # 11. DATA STRUCTURES & ALGORITHMS (4 Books)
    # ==========================================
    {
        "title": "Introduction to Algorithms (4th Edition)",
        "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
        "isbn": "9780262046305",
        "category": "Data Structures & Algorithms",
        "publication_year": 2022,
        "total_copies": 4,
        "description": "The globally renowned 'CLRS' textbook delivering in-depth, rigorous coverage of sorting, dynamic programming, greedy algorithms, and graph theory."
    },
    {
        "title": "Cracking the Coding Interview",
        "author": "Gayle Laakmann McDowell",
        "isbn": "9780984782857",
        "category": "Data Structures & Algorithms",
        "publication_year": 2015,
        "total_copies": 5,
        "description": "189 programming questions and solutions covering big O notation, trees, graphs, heaps, system design, and algorithmic problem-solving techniques."
    },
    {
        "title": "Algorithms (4th Edition)",
        "author": "Robert Sedgewick, Kevin Wayne",
        "isbn": "9780321573513",
        "category": "Data Structures & Algorithms",
        "publication_year": 2011,
        "total_copies": 4,
        "description": "A standard university survey of modern algorithms and data structures with visual diagrams, empirical comparisons, and Java implementations."
    },
    {
        "title": "Grokking Algorithms: An Illustrated Guide",
        "author": "Aditya Y. Bhargava",
        "isbn": "9781617292231",
        "category": "Data Structures & Algorithms",
        "publication_year": 2016,
        "total_copies": 5,
        "description": "A friendly, visual, and beginner-approachable illustrated guide that explains search, sorting, recursion, Dijkstra's algorithm, and dynamic programming."
    },

    # ==========================================
    # 12. BUSINESS & FINANCE (5 Books)
    # ==========================================
    {
        "title": "The Intelligent Investor",
        "author": "Benjamin Graham",
        "isbn": "9780060555665",
        "category": "Business & Finance",
        "publication_year": 1949,
        "total_copies": 4,
        "description": "The greatest book on value investing ever written, teaching investors emotional discipline, margin of safety, and Mr. Market market psychology."
    },
    {
        "title": "Rich Dad Poor Dad",
        "author": "Robert T. Kiyosaki",
        "isbn": "9781612680194",
        "category": "Business & Finance",
        "publication_year": 1997,
        "total_copies": 5,
        "description": "Contrasts the financial philosophies of two father figures to teach financial literacy, cash flow management, and acquiring income-generating assets."
    },
    {
        "title": "Zero to One: Notes on Startups, or How to Build the Future",
        "author": "Peter Thiel, Blake Masters",
        "isbn": "9780804139298",
        "category": "Business & Finance",
        "publication_year": 2014,
        "total_copies": 4,
        "description": "Venture capitalist Peter Thiel provides contrarian insights into creating breakthrough technology monopolies that take society from zero to one."
    },
    {
        "title": "Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts",
        "author": "Annie Duke",
        "isbn": "9780735216358",
        "category": "Business & Finance",
        "publication_year": 2018,
        "total_copies": 4,
        "description": "Former World Series of Poker champion Annie Duke shows how to make sound strategic choices under uncertainty without succumbing to outcome bias."
    },
    {
        "title": "Good to Great: Why Some Companies Make the Leap... and Others Don't",
        "author": "Jim Collins",
        "isbn": "9780066620992",
        "category": "Business & Finance",
        "publication_year": 2001,
        "total_copies": 4,
        "description": "A research-backed management study identifying the key disciplines, hedgehog concepts, and Level 5 leadership that propel good firms to great performance."
    }
]
