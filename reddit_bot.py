import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from movie_creator import create_video
from voice_creator import post_to_speach, comment_to_speach
import secret

def collect_data():
    reddit = secret.client

    now = int(time.time())
    posts = []

    for submission in reddit.subreddit("askreddit").top(time_filter="day", limit=12):
        if (submission.over_18):
            continue
        hoursAgoPosted = (now - submission.created_utc) / 3600
        print(f"[{len(posts)}] {submission.title}     {submission.score}    {'{:.1f}'.format(hoursAgoPosted)} hours ago")
        posts.append(submission)
        if (len(posts) >= 4):
            break

    print(posts)
    decision = input("Choose your question: ")
    post = posts[int(decision)]

    comments = []

    for comment in post.comments:
        if  len(comment.body) > 200:
            continue

        comments.append(comment)
        if len(comments) == 5:
            break

    options = webdriver.ChromeOptions() 
    userdatadir = 'C:/Users/komod/AppData/Local/Google/Chrome/User Data'
    options.add_argument(f"--user-data-dir={userdatadir}")
    driver = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", chrome_options=options)


    driver.maximize_window()
    driver.get(post.url)
    wait = WebDriverWait(driver, 10)
    post_element = driver.find_element(By.ID, f"t3_{post}")
    print(f"Post {post} found. Saving it as png file.")
    post_screenshot = post_element.screenshot_as_png
    with open("ss/question_screenshot.png", "wb") as f:
        f.write(post_screenshot)
    comment_id = 0
    for comment in comments:
        while True:
            try:
                print(f"Comment {comment} found. Saving it as png file.")
                comment_element = driver.find_element(By.ID, f"t1_{comment}")
                comment_screenshot = comment_element.screenshot_as_png
                with open(f"ss/comments/comment_{comment_id+1}.png", "wb") as f:
                    f.write(comment_screenshot)
                comment_id+=1
                break
            except:
                print(f"Comment {comment}  not in scope. Perform window scroll.")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(2)
    driver.quit()

    post_to_speach(post.title)

    for index, comment in enumerate(comments):
        comment_to_speach(comment.body, index+1)

    create_video()

def main():
    choice = input("Do you want to collect new data (y/n)? ")
    if choice.lower() == 'y':
        collect_data()
    elif choice.lower() == 'n':
        create_video()

if __name__ == '__main__':
    main()
