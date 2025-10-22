# AlgoSec AFA Sizing & Licensing Calculator

def calculate_resources(num_firewalls, avg_rules, avg_objects, delta_change_rate, analysts):
    total_rules = num_firewalls * avg_rules
    total_objects = num_firewalls * avg_objects
    delta_devices = int(num_firewalls * delta_change_rate)
    
    print("AFA Deployment Sizing Summary")
    print("-" * 40)
    print(f"Total Firewalls Managed: {num_firewalls}")
    print(f"Total Rulebase Size: {total_rules}")
    print(f"Total Object Complexity: {total_objects}")
    print(f"Daily Delta Analyses: {delta_devices}")
    print(f"Monthly Simulations: {analysts * 5 * 4}")
    
    # CPU Recommendation
    if num_firewalls <= 50:
        cpu = 8
        ram = 32
    elif num_firewalls <= 150:
        cpu = 16
        ram = 64
    else:
        cpu = 32
        ram = 128
    
    storage_gb = 100 + (num_firewalls * 5)
    storage_gb = max(storage_gb, 500)

    print("\n🖥️ Recommended VM Specs:")
    print(f"vCPU: {cpu} cores")
    print(f"RAM: {ram} GB")
    print(f"Storage: {storage_gb} GB (SSD/NVMe recommended)")
    print(f"Disk IOPS: Minimum 300 MB/s")
    
    # Licensing Estimate
    license_blocks = ((num_firewalls // 10) + 1) * 10
    print(f"\n Licensing Blocks: {license_blocks} firewall clusters")
    print(f"Suggested License: 'Preferred Subscription' (includes Risk + Compliance + API)")
    print("-" * 40)

# 🧩 Customize your environment here
calculate_resources(
    num_firewalls=220,          # Total firewalls and cloud controls
    avg_rules=550,              # Average rules per device
    avg_objects=700,            # Average network/service objects per device
    delta_change_rate=0.20,     # 20% of firewalls change daily
    analysts=12                 # Number of AlgoSec analysts
)
