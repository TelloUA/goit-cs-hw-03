def make_queries(connection, sql_file_path):
    try:
        with open(sql_file_path, 'r') as file:
            sql_queries = file.read()
        
        queries = sql_queries.split(';')
        
        with connection.cursor() as cursor:
            for query in queries:
                query = query.strip()
                if not query:
                    continue
                
                try:
                    cursor.execute(query)
                    
                    if cursor.description:
                        results = cursor.fetchall()
                        print(f"Results for query:\n{query}\n{results}\n")
                    else:
                        print(f"Query executed successfully: {query}")
                
                except Exception as e:
                    print(f"Error executing query:\n{query}\n{e}")
        
        connection.commit()

    except Exception as e:
        print(f"Error reading or executing SQL file: {e}")
