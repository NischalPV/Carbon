using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Carbon.Identity.Data.Migrations.IdentityServer.ConfigurationDb
{
    /// <inheritdoc />
    public partial class dataclientsGranttypeupdate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 7, 9, 23, 239, DateTimeKind.Utc).AddTicks(2510));

            migrationBuilder.UpdateData(
                table: "ClientGrantTypes",
                keyColumn: "Id",
                keyValue: 2,
                column: "GrantType",
                value: "authorization_code");

            migrationBuilder.UpdateData(
                table: "Clients",
                keyColumn: "Id",
                keyValue: 2,
                column: "RequirePkce",
                value: true);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 6, 47, 9, 723, DateTimeKind.Utc).AddTicks(9990));

            migrationBuilder.UpdateData(
                table: "ClientGrantTypes",
                keyColumn: "Id",
                keyValue: 2,
                column: "GrantType",
                value: "implicit");

            migrationBuilder.UpdateData(
                table: "Clients",
                keyColumn: "Id",
                keyValue: 2,
                column: "RequirePkce",
                value: false);
        }
    }
}
