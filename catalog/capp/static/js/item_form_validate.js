// validation for item_form.html used in item_add.html

$(function () {
  "use strict";

  // pull out DOM elements
  var item_form = document.forms[0];
  var _submit = item_form.submit;
  var alert_div = $('.alert')[0];
  var submit_btn = $(item_form).find('button')[0];

  // reusabale functions for rules
  // val: value input value for the given rule
  // cb: a callback that takes an error message
  //     as its only argument if there's an error and
  //     undefined if there's not an error
  var rule_non_empty = function (val, cb) {
      if (val.trim() === '') {
        cb("may not be empty");
      } else {
        cb(undefined);
      }
  };

  var rule_title_no_dup = function (val, cb) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          var item_resp_json = JSON.parse(xhr.responseText);
          var item_titles = item_resp_json['Items']
                .map(function (item_json) {
                  return item_json['title'];
                });
          if (item_titles.indexOf(val.trim()) !== -1) {
            cb("Duplicate item name");
          } else {
            cb(undefined);
          }
        } else {
          // ??? how to handle validation w/o server data?
          cb(undefined);
        }
      }
    };
    xhr.open('GET', '/api/item');
    xhr.send();
  };

  // map inputs to rules
  var rules = {
    'title': [
      rule_non_empty,
      rule_title_no_dup
    ],
    'description': [
      rule_non_empty
    ]
  };

  var checks = {};
  var errors = {};

  var reset_checks = function () {
    Object.keys(rules).forEach(function (r_name) {
      checks[r_name] = 0;
    });
  };

  var reset_errors = function () {
    Object.keys(rules).forEach(function (r_name) {
      errors[r_name] = 0;
    });
  };

  var has_errors = function () {
    return Object.keys(rules).filter(function (r_name) {
      return rules[r_name].length - checks[r_name] !== 0;
    }).length !== 0;
  };

  var validation_finished = function () {
    return Object.keys(rules).filter(function (r_name) {
      return rules[r_name].length === checks[r_name] + errors[r_name];
    }).length === Object.keys(rules).length;
  };

  var get_form_elem = function(r_name) {
    var elem = $(item_form.elements) // .elements is not an array
          .toArray().filter(function (elem) {
            return elem.name === r_name;
          })[0];
    if (elem === undefined) {
      throw new Error("rule name does not correspond to input name");
    }
    return elem;
  };

  var get_form_grp = function (r_name) {
    var elem = get_form_elem(r_name);
    return elem.parentNode;
  };

  var make_rule_cb = function(r_name, prev_cb) {
    var form_grp = get_form_grp(r_name);
    var make_help_block = function (help_text) {
      return '<span class="help-block">' + help_text + '</span>';
    };
    return function(help_text) {
      if (help_text !== undefined) {
        $(form_grp).addClass('has-error');
        $(form_grp).append(make_help_block(help_text));
        console.log("error for "+r_name);
        errors[r_name] += 1;
      } else {
        console.log("check for "+r_name);
        checks[r_name] += 1;
      }
      prev_cb();
    };
  };

  // ??? might be better to listen to the submit event
  // rather than wire up an onclick method
  item_form.submit = function (ev) {
    ev.preventDefault();
    // reset state in js and dom
    reset_checks();
    reset_errors();
    Object.keys(rules).forEach(function (r_name) {
      var form_grp = get_form_grp(r_name);
      $(form_grp).removeClass('has-error');
      $(form_grp).find('.help-block').remove();
    });
    alert_div.hidden = true;

    var validation_finished_cb = function () {
      if (has_errors()) {
        alert_div.hidden = false;
      } else {
        _submit.call(item_form);
      }
    };

    var prev_cb = undefined;
    var curr_cb;

    // normally using an async library would be preferable,
    // but just as an exercise in using callbacks...
    // todo: handle the case where Object.keys(rules).length === 0
    // todo: run all callbacks simultaneously
    //       like Promise.all() rather than Promise.next()
    Object.keys(rules).forEach(function (r_name) {
      rules[r_name].forEach(function (rule) {
        if (prev_cb === undefined) {
          prev_cb = validation_finished_cb;
        }
        curr_cb = (function (r_name, prev_cb) {
          return function () {
            rule(get_form_elem(r_name).value,
                 make_rule_cb(r_name, prev_cb));
          };
        }(r_name, prev_cb));
        prev_cb = curr_cb;
      });
    });

    curr_cb();

  };

  submit_btn.onclick = item_form.submit;

});
