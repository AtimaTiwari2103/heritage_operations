"""
=========================================================
Heritage Operations Center
Environment Configuration
=========================================================
"""

# ==========================================================
# Common Settings
# ==========================================================

DEFAULT_SSH_TIMEOUT = 20
DEFAULT_VERIFY_INTERVAL = 5
DEFAULT_VERIFY_RETRY = 24

# ==========================================================
# Environment Configuration
# ==========================================================

ENVIRONMENTS = {

    # ======================================================
    # FLDEV
    # ======================================================

    "FLDEV": {

        "display_name": "FLDEV",

        "color": "#16a34a",

        "icon": "fa-solid fa-server",

        "enabled": True,

        "services": {

            "application_rules": {

                "name": "Application + Rules",

                "host": "",

                "username": "",

                "password": "",

                "port": "49090",

                "jboss_home": "",

                "start_script": "startup_jboss_49090.sh"

            },

            "application": {

                "name": "Application",

                "host": "",

                "username": "",

                "password": "",

                "port": "58181",

                "jboss_home": "",

                "start_script": "startup_jboss_58181.sh"

            },

            "nbic": {

                "name": "NBIC Rating",

                "host": "",

                "username": "",

                "password": "",

                "port": "8780",

                "jboss_home": "",

                "start_script": "startJBOSS"

            },

            "hpci": {

                "name": "HPCI Rating",

                "host": "",

                "username": "",

                "password": "",

                "port": "8480",

                "jboss_home": "",

                "start_script": "startJBOSS"

            }

        }

    },

    # ======================================================
    # QC4
    # ======================================================

    "QC4": {

        "display_name": "QC4",

        "color": "#2563eb",

        "icon": "fa-solid fa-cloud",

        "enabled": True,

        "services": {

            "application_rules": {

                "name": "Application + Rules",

                "host": "",

                "username": "",

                "password": "",

                "port": "9090",

                "jboss_home": "",

                "start_script": "startJBOSS"

            },

            "application": {

                "name": "Application",

                "host": "",

                "username": "",

                "password": "",

                "port": "58080",

                "jboss_home": "",

                "start_script": "startJBOSS"

            },

            "nbic": {

                "name": "NBIC Rating",

                "host": "",

                "username": "",

                "password": "",

                "port": "8780",

                "jboss_home": "",

                "start_script": "startJBOSS"

            },

            "hpci": {

                "name": "HPCI Rating",

                "host": "",

                "username": "",

                "password": "",

                "port": "8480",

                "jboss_home": "",

                "start_script": "startJBOSS"

            }

        }

    },

    # ======================================================
    # ICM
    # ======================================================

    "ICM": {

        "display_name": "ICM",

        "color": "#9333ea",

        "icon": "fa-solid fa-network-wired",

        "enabled": True,

        "services": {

            "DEV": {

                "name": "DEV ICM",

                "host": "",

                "username": "",

                "password": "",

                "port": "8480",

                "jboss_home": "",

                "start_script": "startJBOSS"

            },

            "QC4": {

                "name": "QC4 ICM",

                "host": "",

                "username": "",

                "password": "",

                "port": "9080",

                "jboss_home": "",

                "start_script": "startJBOSS"

            }

        }

    },

    # ======================================================
    # JBEAM
    # ======================================================

    "JBEAM": {

        "display_name": "JBEAM",

        "enabled": True

    },

    # ======================================================
    # SSH
    # ======================================================

    "SSH": {

        "display_name": "SSH",

        "enabled": True

    }

}
