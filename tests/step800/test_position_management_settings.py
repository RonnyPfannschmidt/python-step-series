#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ensure system commands and responses execute successfully."""


import pytest

from stepseries import commands, responses, step800


@pytest.mark.skip_800_disconnected
class TestPositionManagementSettings:

    # Position presets
    run_motor: bool = False

    def test_position(self, device: step800.STEP800) -> None:
        device.set(commands.SetPosition(1, -99999))
        resp = device.get(commands.GetPosition(1))
        assert isinstance(resp, responses.Position)
        assert resp.ABS_POS == -99999

    def test_reset_pos(self, device: step800.STEP800) -> None:
        device.set(commands.ResetPos(1))
        resp: responses.Position = device.get(commands.GetPosition(1))
        assert resp.ABS_POS == 0

    def test_el_pos(self, device: step800.STEP800) -> None:
        device.set(commands.SetElPos(3, 2, 66))
        resp = device.get(commands.GetElPos(3))
        assert isinstance(resp, responses.ElPos)
        assert resp.fullstep == 2
        assert resp.microstep == 66

    def test_mark(self, device: step800.STEP800) -> None:
        device.set(commands.SetMark(1, 123456))
        resp = device.get(commands.GetMark(1))
        assert isinstance(resp, responses.Mark)
        assert resp.MARK == 123456

    def test_go_home(self, device: step800.STEP800) -> None:
        if self.run_motor:
            device.set(commands.GoHome(1))
        else:
            pytest.skip("preset 'run_motor' is not set")

    def test_go_mark(self, device: step800.STEP800) -> None:
        if self.run_motor:
            device.set(commands.GoMark(1))
        else:
            pytest.skip("preset 'run_motor' is not set")
