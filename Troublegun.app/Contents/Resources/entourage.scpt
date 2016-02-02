tell application "Microsoft Entourage"
  set theRecipients to {{address:{display name:"%@", address:"%@"}, recipient type:to recipient}}
  set theMessage to make new outgoing message with properties {recipient:theRecipients, subject:"%@", attachment:{file:(POSIX file "%@")}}
  open theMessage
  activate
end tell
