# BuiltOn Python SDK
> Python SDK for the BuiltOn APIs

![PyPI](https://img.shields.io/pypi/v/builton-sdk.svg)
![PyPI - Status](https://img.shields.io/pypi/status/builton-sdk.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dd/builton-sdk.svg)

[![Builton logo](https://res.cloudinary.com/dftspnwxo/image/upload/v1554131594/Builton_logo_positiv_wc3j7x.svg)](https://builton.dev)

[BuiltOn](https://builton.dev) offers a platform as a service that digitizes core business functions and optimizes 
resource allocation with baked-in machine learning capabilities. 
This package gives you access to our platform's building blocks and will help you implement its API.
 Get instant access to modules like Payments, Messaging Tools, User Management, Scheduling, 
 Resource Allocation and more.

## Documentation

See the [BuiltOn API documentation](https://docs.builton.dev) for a full reference of the API or visit
our website - [https://builton.dev](https://builton.dev) - if you want to create an account.

## Getting Started

### Prerequisites

This package has been fully tested using Python 3.6, but it's expected to work in 
all Python 3+ versions.

### Installation

To install the package use pip as usual:
```bash
pip install --upgrade builton-sdk
```

To install from source use:
```bash
python setup.py install
```

## Usage

```python
from builton_sdk import Builton
builton = Builton(api_key="API_KEY", bearer_token="BEARER_TOKEN")
builton.product().get_all({"size": 1})
``` 

The `API_KEY` and the `BEARER_TOKEN` are both in the [Settings](https://dashboard.builton.dev/settings) 
section of your BuiltOn dashboard. The `API_KEY` will be under **API Keys** and if you don't have one
yet, please go ahead and create it. The `BEARER_TOKEN` you can fetch from the **Service Accounts** 
section, from an existing Service Account or by creating a new one.

## Contributing

### Configuration

Before starting to use the package, please copy the `config.py.template` into 
`config.py` and edit the configuration inside accordingly. Have a look at the [Usage](#usage) section 
for more information on how to find the values to put inside the `config.py`.

### Testing

Our test suite depends heavily on [talkback](https://github.com/ijpiantanida/talkback) to mock some 
of the API responses. So, in order to contribute you'll need to first have node.js and npm installed 
and then you can run the following script to start the talkback server: 

```bash
./tests/integration/scripts/run_server.sh
```

After the server starts, you can put it in background and then run the tests:

```bash
python -m pytest tests/
```

### Pushing Changes

Follow the steps below to open a new Pull Request into this package:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b amazing-feature`)
3. Commit your Changes (`git commit -m 'Add some Amazing Feature'`)
4. Push to the Branch (`git push origin amazing-feature`)
5. Open a Pull Request


## License

This project is licensed under the MIT license. See the [LICENSE](LICENSE.md) file for more info.

## Contact

Please use the github issues for problems you find with the package or suggestions for changes.

If you need to get in touch with anyone from our team please email us at 
[hello@builton.dev](mailto:hello@builton.dev)
