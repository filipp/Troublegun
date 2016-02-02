tell application "Mail"
  set theMessage to make new outgoing message with properties {visible:true, subject:"$subject", content:"$message"}
  tell theMessage
    make new to recipient at end of to recipients with properties {name:"$name", address:"$address"}
    end tell
    tell content of theMessage
      make new attachment with properties {file name:"$filename"}
    end tell
    activate
end tell
