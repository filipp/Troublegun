### What is the meaning of this?

[Troublegun](https://github.com/filipp/Troublegun) is a simple tool for collecting error reports from end users to help
admins with troubleshooting. The idea is to make it as easy as possible for end users
to send helpful troubleshooting info when problems occur.

### System Requirements

- Mac OS X (tested with 10.8 and 10.9)
- Python 2.7 or later
- Mail.app or Microsoft Entourage


### Configuration

Navigate to __Troublegun.app > Show package contents > Contents > Resources__ and edit config.ini to your liking.

Here's an example:

    [message]
    name: Our IT guy
    address: you@example.com
    subject: Problem Report
    message: Application:
      Problem:

    attachments: screencapture

Save the file, copy the app to your users' Applications_-folder, add it to their dock.

### License

The MIT License (MIT)
Copyright (c) 2016 Filipp Lepalaan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


### Thanks

Icon provided by flaticons.net
