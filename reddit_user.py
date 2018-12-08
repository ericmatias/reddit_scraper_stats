


class RedditUserData:


    data_types = {"t1" : "comment"
                , "t2" : "account"
                , "t3" : "link"
                , "t4" : "message"
                , "t5" : "subreddit"
                , "t6" : "award"}

    def __init__(self, username, driver):

        self.username = username
        self.driver = driver



    #   Get Comment Data stats

    def get_sub_commented(self):
        pass

    def time_sub_was_commented(self):
        pass

    def comment_text(self):
        pass

    def number_of_comments_in_sub_commented_in(self):
        pass

    def get_all_subs_commented(self):
        pass

    #   Post Submission Data stats

    def get_all_subs_post_submitted(self):
        pass

    def post_submitted_title(self):
        pass

    def time_post_submitted(self):
        pass

    def number_of_comments_in_sub_posted_in(self):
        pass


    # Random utils, etc.

    def get_sub_quaratine_status(self):
        pass

    def convert_unixtimestamp_to_ymdhms(self):
        pass

    def write_all_raw_data_to_flat_file(self):
        pass