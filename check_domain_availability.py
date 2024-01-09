import whois

def check_domain_availability(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        if domain_info.status:
            print(f"The domain '{domain_name}' is already registered.")
        else:
            print(f"The domain '{domain_name}' is available for registration!")
    except AttributeError:
        print("An error occurred while checking the domain availability.")

if __name__ == "__main__":
    domain_to_check = input("Enter the domain name you want to check: ")

    check_domain_availability(domain_to_check)
