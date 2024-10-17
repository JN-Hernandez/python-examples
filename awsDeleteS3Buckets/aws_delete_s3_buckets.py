"""
Delete S3 Buckets within AWS
"""
import boto3

S3_RESOURCE = boto3.resource("s3")
S3_CLIENT = boto3.client("s3")

def get_all_s3_buckets():
    """Gets list of all S3 buckets within AWS Account and returns list"""
    response = S3_CLIENT.list_buckets()
    bucket_list = []
    for bucket in response["Buckets"]:
        bucket_list.append(bucket["Name"])
    return bucket_list


def delete_bucket(bucket):
    """Deletes S3 bucket contents then bucket itself"""
    bucket_to_delete = S3_RESOURCE.Bucket(bucket)
    contents = []
    for object_key in bucket_to_delete.objects.all():
        contents.append(object_key.key)
    if not contents:
        user_confirmation = input("Bucket is empty, continue to delete? [y/n] ")
        if user_confirmation.lower() in ["y", "yes"]:
            print(f"Deleting \"{bucket}\"...", end="")
            S3_RESOURCE.Bucket(bucket).delete()
            print(" done!")
        elif user_confirmation.lower() in ["n", "no"]:
            print(f"Skipping \"{bucket}\"")
    if contents:
        delete_bucket_contents(bucket, contents)


def delete_bucket_contents(bucket, contents):
    for file in contents:
        print(f"- {file}")
    user_confirmation = input("\n\nContinue to delete bucket? [y/n] ")
    if user_confirmation.lower() in ["y", "yes"]:
        print(f"Deleting \"{bucket}\"...", end="")
        print(" done!")
    elif user_confirmation.lower() in ["n", "no"]:
        print(f"Skipping \"{bucket}\"")


def main():
    print("Gathering list of S3 buckets...", end="")
    bucket_list = get_all_s3_buckets()
    print(" done!\n\nThis script will now iterate through each bucket to \
determine what to delete.  \nPlease note that this action CANNOT be undone!")
    for bucket in bucket_list:
        user_decision = input(f"\nDelete bucket \"{bucket}\"?  [y/n] ")
        if user_decision.lower() in ["y","yes"]:
            print(f"\nReviewing {bucket} and its contents:\n")
            delete_bucket(bucket)
        elif user_decision.lower() in ["n", "no"]:
            print(f"Skipping {bucket}.")
        else:
            print(f"\n\nUnknown input!  Please enter y/n or yes/no.")
            break


if __name__ == "__main__":
    main()