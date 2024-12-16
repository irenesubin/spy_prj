import mysql.connector
import openai

OPENAI_API_KEY = os.getenv#('your openapi key')

# 데이터베이스 연결 설정
db_config = {
    'host': #'yourdb Ip address',
    'user': #'yourdb user name',
    'password': #'yourdb pw',
    'database': #'yourdb table name'
}

# 수정할 테이블 목록
tables = ['web', 'linux', 'windows']

#gpt-4에 쉘코드를 보내고 요청값을 반환
def get_analysis(shell_code):
    prompt = f"이 쉘 코드를 어셈블리어로 바꿔줘: {shell_code}\n1. 해석도 포함해서\n2. 이 코드는 어떤 os에 사용가능해?\n3. 이 코드는 어떤 os 버전에 사용 가능한지 알려줘."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    analysis_result = response['choices'][0]['message']['content']
    return analysis_result


# 각 테이블에서 데이터를 수정
for table in tables:
    select_query = f"SELECT id, content FROM {table} WHERE analysis_result IS NULL"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    
    for row in rows:
        shell_code_id = row[0]
        shell_code = row[1]
        
        # GPT-4로 분석 요청
        analysis_result = get_analysis(shell_code)
        
        # 분석 결과를 데이터베이스에 업데이트
        update_query = f"UPDATE {table} SET analysis_result = %s WHERE id = %s"
        cursor.execute(update_query, (analysis_result, shell_code_id))
    
    # 변경 사항 커밋
    db_connection.commit()

# 커서와 연결 종료
cursor.close()
db_connection.close()

print("모든 데이터 분석 완료!")
