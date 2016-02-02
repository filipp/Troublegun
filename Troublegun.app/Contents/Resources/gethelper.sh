defaults read com.apple.launchservices LSHandlers | grep -B 1 mailto | grep RoleAll | awk 'IFS="=" { print $3; }'
