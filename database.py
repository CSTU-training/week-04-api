'''
Author: Telliex telliexyuzo@gmail.com
Date: 2026-05-30 21:00:27
LastEditors: Telliex telliexyuzo@gmail.com
LastEditTime: 2026-05-30 21:02:53
FilePath: /week-04-api/database.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
    
"""
    Create a database.py file for a FastAPI + SQLAlchemy setup that:
1. Reads DATABASE_URL from an environment variable using python-dotenv
2. Creates a SQLAlchemy engine
3. Creates a SessionLocal factory
4. Creates a Base class for models to inherit from
5. Provides a get_db() dependency function that yields a session and closes it
Include comments explaining each part.
"""