JS_DROP_FILE = """
    var target = arguments[0],
        offsetX = arguments[1],
        offsetY = arguments[2],
        document = target.ownerDocument || document,
        window = document.defaultView || window;

    var input = document.createElement('INPUT');
    input.type = 'file';
    input.onchange = function () {
      var rect = target.getBoundingClientRect(),
          x = rect.left + (offsetX || (rect.width >> 1)),
          y = rect.top + (offsetY || (rect.height >> 1)),
          dataTransfer = { files: this.files };

      ['dragenter', 'dragover', 'drop'].forEach(function (name) {
        var evt = document.createEvent('MouseEvent');
        evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
        evt.dataTransfer = dataTransfer;
        target.dispatchEvent(evt);
      });

      setTimeout(function () { document.body.removeChild(input); }, 25);
    };
    document.body.appendChild(input);
    return input;
"""
groupsFacebookUrl = [
    "Royalcityhanoi",
    "chocudanlangroyalcity",
    "415565940789802",
    "1215795799391969",
    "141324381894784",
    "110881122672542",
    "817099596614059",
    "1412788409534990",
    "481698580782388",
    "585361611486409",
    # "985101529134280",
    # "145842068876936",
    # "chothuephongtrochungcuhanoi",
    # "595801192447347",
    # "198770455230229",
    # "166558550584705",
    # "370527694023091",
    # "754896778782109",
    # "726296189285168",
    # "timescity.parkhill86",
    # "muabanchothuecanhochungcudcapitale",
    # "173239365588121",
    # "751148002230787",
    # "235093308909899",
    # "219292898527854",
    # "890020662052282",
    # "659542662847798",
    # "617608536363897",
    # "158625242808646",
    # "346244929095372",
]

facebookUrl = "https://facebook.com"
driverPath = "./app/chromedriver.exe"
